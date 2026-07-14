app_name = "oidc_group"
app_title = "OIDC Group"
app_publisher = "VT"
app_description = "Sync OIDC group"
app_email = "vt@lab.spaceac.tech"
app_license = "mit"

# Send non-GET requests for this app's endpoints as native `application/json`
# bodies instead of form-encoded, per-key JSON-stringified values.
use_json_request_body = True

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "oidc_group",
# 		"logo": "/assets/oidc_group/logo.png",
# 		"title": "OIDC Group",
# 		"route": "/oidc_group",
# 		"has_permission": "oidc_group.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/oidc_group/css/oidc_group.css"
# app_include_js = "/assets/oidc_group/js/oidc_group.js"

# include js, css files in header of web template
# web_include_css = "/assets/oidc_group/css/oidc_group.css"
# web_include_js = "/assets/oidc_group/js/oidc_group.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "oidc_group/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "oidc_group/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "oidc_group.utils.jinja_methods",
# 	"filters": "oidc_group.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "oidc_group.install.before_install"
# after_install = "oidc_group.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "oidc_group.uninstall.before_uninstall"
# after_uninstall = "oidc_group.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "oidc_group.utils.before_app_install"
# after_app_install = "oidc_group.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "oidc_group.utils.before_app_uninstall"
# after_app_uninstall = "oidc_group.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "oidc_group.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "oidc_group.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"oidc_group.tasks.all"
# 	],
# 	"daily": [
# 		"oidc_group.tasks.daily"
# 	],
# 	"hourly": [
# 		"oidc_group.tasks.hourly"
# 	],
# 	"weekly": [
# 		"oidc_group.tasks.weekly"
# 	],
# 	"monthly": [
# 		"oidc_group.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "oidc_group.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "oidc_group.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------

override_whitelisted_methods = {
	# Override OIDC login endpoints to capture groups from userinfo and sync Frappe roles.
	# "custom" covers all Social Login Keys (Auth0, Okta, Authentik, etc.)
	"frappe.integrations.oauth2_logins.custom": "oidc_group.auth.custom",
	"frappe.integrations.oauth2_logins.login_via_keycloak": "oidc_group.auth.login_via_keycloak",
}

# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "oidc_group.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["oidc_group.utils.before_request"]
# after_request = ["oidc_group.utils.after_request"]

# Job Events
# ----------
# before_job = ["oidc_group.utils.before_job"]
# after_job = ["oidc_group.utils.after_job"]

# after_file_upload = ["oidc_group.utils.after_file_upload"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"oidc_group.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

