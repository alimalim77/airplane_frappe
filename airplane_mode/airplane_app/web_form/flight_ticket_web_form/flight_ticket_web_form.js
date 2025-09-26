console.log("Flight Ticket Web Form script loaded");    
frappe.ready(function () {
	// bind events here
	frappe.web_form.on('flight', function() {
		var flight_value = frappe.web_form.get_value('flight');
		frappe.call({
			method: 'frappe.client.get_list',
			args: {
				doctype: 'Airplane Ticket',
				fields: ['name', 'flight', 'seat', "flight_ticket"], // add more fields as needed
				filters: {
					flight: flight_value
				}
			},
			callback: function(r) {
				if (r.message && r.message.length > 0) {
					console.log("Matching Airplane Ticket records:", r.message);
				} else {
					console.log("No Airplane Ticket records found for flight:", flight_value);
				}
				console.log("Setting flight_ticket field value to:", r.message[0].flight_ticket);		
				frappe.web_form.set_value('flight_ticket', r.message[0].flight_ticket);
			}
		});
	});
})


