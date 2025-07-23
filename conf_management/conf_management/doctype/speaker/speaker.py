# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Speaker(Document):
	# def autoname(self):
	# 	self.name = "sdsdd"

	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"

	def on_trash(self):
		frappe.throw("You can't delete this!")
