# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
import qrcode
from frappe.model.document import Document


class Ticket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from conf_management.ticketing.doctype.ticket_check_in.ticket_check_in import TicketCheckIn

		attendee_name: DF.Data | None
		check_ins: DF.Table[TicketCheckIn]
		conference: DF.Link
		email: DF.Data
		has_qr: DF.Check
		qr_code: DF.AttachImage | None
		registration: DF.Link | None
	# end: auto-generated types

	def after_insert(self):
		# frappe.enqueue("conf_management.tasks.finalise_tickets", queue="long")
		# frappe.enqueue_doc("Ticket", self.name, "generate_qr_code")
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

	def on_update(self):
		pass


@frappe.whitelist(allow_guest=True)
def check_in(doctype, doc_name):
	return frappe.get_doc(doctype, doc_name)


# def on_doctype_update():
# 	frappe.db.add_index("Ticket", ["ticket_type", "conference"])
