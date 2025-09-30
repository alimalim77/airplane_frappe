import frappe
from frappe import _
from frappe.query_builder.functions import Sum
from collections import defaultdict

def execute(filters=None):
	columns = [
		{
			"fieldname": "airline",
			"label": _("Airline"),
			"fieldtype": "Link",
			"options": "Airline",
			"width": 200
		},
		{
			"fieldname": "revenue",
			"label": _("Revenue"),
			"fieldtype": "Currency",
			"width": 150
		}
	]

	# Get all airlines to include those with zero revenue
	airlines = frappe.get_all("Airline", pluck="name")
	
	# Get revenue data using frappe.get_all instead of query builder
	revenue_data = frappe.get_all(
		"Airplane Ticket",
		filters={"docstatus": 1},  # Only submitted tickets
		fields=[
			"flight as airplane",
			"sum(flight_ticket) as revenue"
		],
		group_by="flight"
	)
	
	# Initialize data structures
	data = []
	revenue_map = defaultdict(float)
	total_revenue = 0

	# Create revenue mapping
	for d in revenue_data:
		airplane = frappe.db.get_value("Airplane Flight", d.airplane, "airplane")
		airline = frappe.db.get_value("Airplane", airplane, "airline")
		revenue_map[airline] += d.revenue
		total_revenue += d.revenue

	print("map for the total revenue obtained is ", revenue_map)
	# Add all airlines, including those with zero revenue
	for airline in airlines:
		data.append({
			"airline": airline,
			"revenue": revenue_map.get(airline, 0)
		})

	# Add total row
	data.append({
		"airline": "Total",
		"revenue": total_revenue,
		"bold": 1
	})

	# Prepare chart (exclude the "Total" row)
	chart = {
		"type": "donut",
		"data": {
			"labels": [d["airline"] for d in data if d["airline"] != "Total"],
			"datasets": [{
				"name": "Revenue Distribution",
				"values": [d["revenue"] for d in data if d["airline"] != "Total"]
			}]
		}
	}
	return columns, data, None, chart
