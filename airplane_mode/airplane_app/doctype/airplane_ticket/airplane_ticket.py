# Copyright (c) 2025, alim and contributors
# For license information, please see license.txt

import frappe
import random

from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class AirplaneTicket(Document):
    def before_save(self):
        # Calculate total amount
        total = 0
        for addon in self.add_ons:
            total += addon.amount
        self.total_amount = total + int(self.flight_ticket)

    def before_insert(self):
        # Generate a random integer (you can specify a range, e.g., 1 to 100)
        random_integer = random.randint(1, 100)

        # Generate a random capital letter from A to E
        random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])

        # Combine them
        self.seat = f"{random_integer}{random_letter}"
                
    def validate(self):
        seen = set()
        unique_addons = []
        for addon in self.add_ons:
            # Assuming 'addon_type' is the field that identifies the type of add-on
            if addon.item not in seen:
                unique_addons.append(addon)
                seen.add(addon.item)
            else:
                # Duplicate found, skip adding it
                pass
        
        self.set("add_ons", unique_addons)
    
    def on_submit(self):
        if self.status != "Boarded":
            frappe.throw("Wrong status picked")
        self.status = "Completed"
