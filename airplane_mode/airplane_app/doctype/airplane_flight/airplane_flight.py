# Copyright (c) 2025, alim and contributors
# For license information, please see license.txt

from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"
