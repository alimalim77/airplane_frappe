# Copyright (c) 2025, alim and contributors
# For license information, please see license.txt


import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"
		# Submit all Airplane Tickets linked to this flight and are Boarded
		tickets = frappe.get_all(
			"Airplane Ticket",
			filters={"status": "Boarded"},
			fields=["name"]
		)
		frappe.errprint(tickets)
		for ticket in tickets:
			try:
				doc = frappe.get_doc("Airplane Ticket", ticket.name)
				if doc.docstatus == 0:
					doc.submit()
				frappe.errrint(f"Submitted ticket {ticket.name}")
			except Exception as e:
				frappe.log_error(f"Error submitting ticket {ticket.name}: {str(e)}", "AirplaneFlight on_submit")