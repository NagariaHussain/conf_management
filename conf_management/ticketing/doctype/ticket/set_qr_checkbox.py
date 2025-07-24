import frappe


def execute():
	frappe.db.set_value("Ticket", {"qr_code": ("is", "set")}, "has_qr", 1, update_modified=False)
	frappe.db.commit()
