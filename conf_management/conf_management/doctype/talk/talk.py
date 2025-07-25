# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Talk(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.TextEditor | None
		naming_series: DF.Literal["TALK-.speaker.-.###", "WORKSHOP-.###"]
		speaker: DF.Link
		title: DF.Data
	# end: auto-generated types

	def before_insert(self):
		# self.speaker
		pass
