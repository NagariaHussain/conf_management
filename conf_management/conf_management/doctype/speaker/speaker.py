# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Speaker(Document):
	# def autoname(self):
	# 	self.name = "sdsdd"

	def before_save(self):
		if self.last_name:
			self.full_name = f"{self.first_name} {self.last_name}"
		else:
			self.full_name = self.first_name

	def on_trash(self):
		frappe.throw("You can't delete this!")
