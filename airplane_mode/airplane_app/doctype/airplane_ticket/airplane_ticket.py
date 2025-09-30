# Copyright (c) 2025, alim and contributors
# For license information, please see license.txt

from annotated_types import doc
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
        try:
            # Generate a random integer (you can specify a range, e.g., 1 to 100)
            airplane_capacity = self.fetch_airplane_details()
            fieldname = "seats"  # Change to your actual field name

            if hasattr(self, "seats") and self.seats > airplane_capacity:
                frappe.throw("No seats available")  
            else:
                if hasattr(self, fieldname):
                    # Get the count of AirplaneTicket records for this flight
                    current_value = frappe.db.count('Airplane Ticket', filters={'flight': self.flight})
                    if current_value is not None:
                        setattr(self, fieldname, current_value + 1)
                    else:
                        frappe.errprint(self.seat, self.seats)
                        setattr(self, fieldname, 1)
                else:
                    setattr(self, fieldname, 1)
        except Exception as e:
            frappe.log_error(f"Error in before_insert: {str(e)}", "AirplaneTicket before_insert")
            frappe.throw(f"An error occurred while assigning seat: {str(e)}")
                

        # try:
        #     # Generate a random integer (you can specify a range, e.g., 1 to 100)
        #     airplane_capacity = self.fetch_airplane_details()
        #     alphabet_mapping = [chr(i) for i in range(65, 91)] 
        #     person_per_alphabet = airplane_capacity // len(alphabet_mapping)

        #     fieldname = "seats"  # Change to your actual field name
        #     initial_value = (alphabet_mapping[0], 1)

        #     if hasattr(self, "seats") and self.seats > airplane_capacity:
        #         frappe.throw("No seats available")  
        #     else:
        #         if hasattr(self, fieldname):
        #             # Get the count of AirplaneTicket records for this flight
        #             current_value = frappe.db.count('Airplane Tsetattr(self, "seat", alphabet_mapping[current_value//person_per_alphabet] + str((current_value%person_per_alphabet) + 1))icket', filters={'flight': self.flight})
        #             if current_value is not None:
        #                 setattr(self, fieldname, current_value + 1)
        #             else:
        #                 frappe.errprint(self.seat, self.seats)
        #                 setattr(self, fieldname, initial_value)
        #             setattr(self, "seat", alphabet_mapping[current_value//person_per_alphabet] + str((current_value%person_per_alphabet) + 1))
        #         else:
        #             setattr(self, fieldname, initial_value)
        # except Exception as e:
        #     frappe.log_error(f"Error in before_insert: {str(e)}", "AirplaneTicket before_insert")
        #     frappe.throw(f"An error occurred while assigning seat: {str(e)}")

                
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


    def fetch_airplane_details(self):
        flight = frappe.get_doc("Airplane Flight", self.flight)
        airplane = frappe.get_doc("Airplane", flight.airplane)
        return airplane.capacity