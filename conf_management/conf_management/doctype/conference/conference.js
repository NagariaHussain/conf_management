// Copyright (c) 2025, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Conference", {
	refresh(frm) {
		frm.add_custom_button("Check In", () => {
			new frappe.ui.Scanner({
				dialog: true, // open camera scanner in a dialog
				multiple: false, // stop after scanning one value
				on_scan(data) {
					const ticket_id = data.decodedText;

					frappe
						.call("conf_management.ticketing.doctype.ticket.ticket.check_in", {
							ticket_id,
						})
						.then(() => {
							frappe.show_alert("Check In Successful!");
						});
				},
			});
		});
	},
});
