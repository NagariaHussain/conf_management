# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
import qrcode
from frappe.model.document import Document


class Ticket(Document):
	def after_insert(self):
		self.generate_qr_code()

	def generate_qr_code(self):
		import io

		payload = {"id": self.name, "name": self.attendee_name}
		img = qrcode.make(frappe.as_json(payload))
		output = io.BytesIO()
		img.save(output, format="PNG")
		hex_data = output.getvalue()

		qr_file = frappe.new_doc("File")
		qr_file.file_name = f"qr-image-{self.name}.png"
		qr_file.content = hex_data
		qr_file.attached_to_doctype = "Ticket"
		qr_file.attached_to_name = self.name
		qr_file.attached_to_field = "qr_code"
		qr_file.save()

		self.qr_code = qr_file.file_url
		self.save()


@frappe.whitelist(allow_guest=True)
def check_in(doctype, doc_name):
	return frappe.get_doc(doctype, doc_name)
