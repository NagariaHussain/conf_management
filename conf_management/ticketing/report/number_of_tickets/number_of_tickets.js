// Copyright (c) 2025, BWH and contributors
// For license information, please see license.txt

frappe.query_reports["Number of Tickets"] = {
	filters: [
		{
			fieldname: "my_filter",
			label: __("My Filter"),
			fieldtype: "Data",
			reqd: 1,
		},
	],
};
