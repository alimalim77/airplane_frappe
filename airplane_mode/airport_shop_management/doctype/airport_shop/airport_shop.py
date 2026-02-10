# Copyright (c) 2026, alim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportShop(Document):
	pass

def send_rent_reminders():
	# Check if reminders are enabled
	settings = frappe.get_single("Airport Shop Settings")
	if not settings.enable_rent_reminders:
		return

	# Send monthly rent reminder emails to all tenants
	shops = frappe.get_all(
		"Airport Shop",
		filters={"tenant_email": ["is", "set"]},
		fields=["name", "tenant_name", "tenant_email", "rent_amount", "shop_number"]
	)
	for shop in shops:
		frappe.sendmail(
			recipients=[shop.tenant_email],
			subject=f"Rent Reminder for Shop {shop.shop_number}",
			message=f"""
				<p>Dear {shop.tenant_name},</p>
				<p>This is a reminder that your monthly rent of
				<b>₹{shop.rent_amount}</b> for Shop <b>{shop.shop_number}</b>
				is due.</p>
				<p>Please make the payment at the earliest.</p>
				<p>Regards,<br>Airport Management</p>
			""",
		)

