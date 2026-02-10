# Copyright (c) 2025, alim and contributors
# For license information, please see license.txt


import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_update(self):
		if self.has_value_changed("gate_number"):
			frappe.enqueue(
				update_gate_in_tickets,
				flight_name=self.name,
				gate_number=self.gate_number,
			)

	def on_submit(self):
		self.status = "Completed"
		# Submit all Airplane Tickets linked to this flight and are Boarded
		tickets = frappe.get_all(
			"Airplane Ticket",
			filters={"flight": self.name, "status": "Boarded"},
			fields=["name"]
		)
		for ticket in tickets:
			try:
				doc = frappe.get_doc("Airplane Ticket", ticket.name)
				if doc.docstatus == 0:
					doc.submit()
			except Exception as e:
				frappe.log_error(f"Error submitting ticket {ticket.name}: {str(e)}", "AirplaneFlight on_submit")


def update_gate_in_tickets(flight_name, gate_number):
	"""Background job to update gate number in all tickets linked to this flight."""
	tickets = frappe.get_all(
		"Airplane Ticket",
		filters={"flight": flight_name},
		pluck="name"
	)
	for ticket_name in tickets:
		frappe.db.set_value("Airplane Ticket", ticket_name, "gate", gate_number)
	frappe.db.commit()