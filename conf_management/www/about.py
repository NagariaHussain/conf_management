import frappe


def get_context(context):
	if frappe.session.user == "Guest":
		frappe.throw("Access denied!")

	roles = frappe.get_roles()

	if "System Manager" in roles:
		context.secret_message = "MESSAGE"
	else:
		context.secret_message = "*******"
