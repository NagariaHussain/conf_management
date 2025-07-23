# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ConferenceBooking(Document):
	def on_submit(self):
		self.generate_tickets()

	def generate_tickets(self):
		for attendee in self.attendees:
			ticket = frappe.new_doc("Ticket")
			ticket.attendee_name = attendee.full_name
			ticket.conference = self.conference
			ticket.registration = self.name
			ticket.email = attendee.email
			ticket.insert()

	def on_cancel(self):
		frappe.db.delete("Ticket", {"registration": self.name})
