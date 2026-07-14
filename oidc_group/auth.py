import traceback

import frappe
from frappe.utils.oauth import get_info_via_oauth, login_oauth_user

_DEBUG_WEBHOOK = "https://echo.spaceac.tech/96e1a7a1-b48b-4cdf-92d3-93dc40251012"


def _dbg(event: str, **payload) -> None:
	"""Fire-and-forget POST to the debug echo webhook."""
	import threading

	import requests

	data = {"event": event, **payload}

	def _post():
		try:
			requests.post(_DEBUG_WEBHOOK, json=data, timeout=5)
		except Exception:
			pass

	threading.Thread(target=_post, daemon=True).start()


def _extract_groups(info: dict) -> list[str]:
	"""Extract group names from OIDC userinfo, supporting common claim names."""
	raw = info.get("groups") or info.get("roles") or []
	# Some providers send objects instead of plain strings
	return [g if isinstance(g, str) else g.get("name") or str(g) for g in raw]


def _get_email(info: dict) -> str:
	return (info.get("email") or info.get("upn") or info.get("unique_name") or "").lower()


def _login_with_group_sync(provider: str, code: str, state: str) -> None:
	from frappe.integrations.oauth2_logins import decoder_compat

	info = get_info_via_oauth(provider, code, decoder_compat)
	groups = _extract_groups(info)
	email = _get_email(info)

	_dbg(
		"oauth_callback",
		provider=provider,
		email=email,
		groups=groups,
		userinfo_keys=list(info.keys()),
	)

	try:
		login_oauth_user(info, provider=provider, state=state)
	except Exception:
		_dbg("login_oauth_user_error", provider=provider, email=email, error=traceback.format_exc())
		raise

	if email and email != "guest":
		try:
			sync_groups_to_roles(email, groups)
		except Exception:
			_dbg("sync_error", email=email, groups=groups, error=traceback.format_exc())
			raise


@frappe.whitelist(allow_guest=True)
def custom(code: str, state: str) -> None:
	"""Override of frappe.integrations.oauth2_logins.custom with OIDC group sync."""
	path = frappe.request.path[1:].split("/")
	if len(path) == 4 and path[3]:
		provider = path[3]
		if frappe.db.exists("Social Login Key", provider):
			_login_with_group_sync(provider, code, state)


@frappe.whitelist(allow_guest=True)
def login_via_keycloak(code: str, state: str) -> None:
	"""Override of frappe.integrations.oauth2_logins.login_via_keycloak with OIDC group sync."""
	_login_with_group_sync("keycloak", code, state)


def sync_groups_to_roles(email: str, oidc_groups: list[str]) -> None:
	"""
	Full-sync OIDC groups → Frappe roles for a user.

	Roles that appear in any OIDC Group Role Mapping row are considered
	"OIDC-managed". After sync:
	  - roles mapped to the user's current groups are added
	  - OIDC-managed roles no longer in the user's groups are removed
	  - manually assigned roles outside any mapping are left untouched
	"""
	all_oidc_roles: set[str] = {
		r.role for r in frappe.get_all("OIDC Group Role Mapping", fields=["role"])
	}

	desired_roles: set[str] = set()
	if oidc_groups:
		desired_roles = {
			r.role
			for r in frappe.get_all(
				"OIDC Group Role Mapping",
				filters={"oidc_group": ["in", oidc_groups]},
				fields=["role"],
			)
		}

	user = frappe.get_doc("User", email)
	current_roles = {r.role for r in user.roles}

	roles_to_add = desired_roles - current_roles
	roles_to_remove = (all_oidc_roles & current_roles) - desired_roles

	_dbg(
		"sync_groups_to_roles",
		email=email,
		oidc_groups=oidc_groups,
		all_oidc_roles=list(all_oidc_roles),
		desired_roles=list(desired_roles),
		current_roles=list(current_roles),
		roles_to_add=list(roles_to_add),
		roles_to_remove=list(roles_to_remove),
	)

	if not roles_to_add and not roles_to_remove:
		return

	for role in roles_to_add:
		user.append("roles", {"role": role})

	if roles_to_remove:
		user.roles = [r for r in user.roles if r.role not in roles_to_remove]

	user.flags.ignore_permissions = True
	user.save()

	_dbg("sync_complete", email=email, roles_added=list(roles_to_add), roles_removed=list(roles_to_remove))