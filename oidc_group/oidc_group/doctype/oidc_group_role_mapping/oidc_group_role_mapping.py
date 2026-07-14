import frappe
from frappe.model.document import Document


class OIDCGroupRoleMapping(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from frappe.types import DF

	oidc_group: DF.Data
	roles: DF.Table["OIDCGroupRole"]
	# end: auto-generated types
	pass
