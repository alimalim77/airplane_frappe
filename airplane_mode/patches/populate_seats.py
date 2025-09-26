import frappe
import random

def execute():
    random_integer = random.randint(1, 100)
    random_letter = random.choice(['S', 'T', 'U', 'V', 'W'])
    print("hello")
    tickets = frappe.get_all("Airplane Ticket", filters={"docstatus": 1}, fields=["name"])

    for ticket in tickets:
        # Directly update the seat field in the database to avoid timestamp mismatch
        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", f"{random_integer}{random_letter}")
        frappe.db.set_value("Airplane Ticket", ticket.name, "is_published_", 1) 
    frappe.db.commit() 