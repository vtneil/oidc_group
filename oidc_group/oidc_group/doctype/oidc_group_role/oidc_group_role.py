import frappe
from frappe.model.document import Document


class OIDCGroupRole(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from frappe.types import DF

	parent: DF.Data
	parentfield: DF.Data
	parenttype: DF.Data
	role: DF.Link
	# end: auto-generated types
	pass
