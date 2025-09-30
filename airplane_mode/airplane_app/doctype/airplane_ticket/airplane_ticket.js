// Copyright (c) 2025, alim and contributors
frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        if ( frm.doc.seat == 0 || frm.doc.seat == ""){
            frm.add_custom_button(('Assign Seats'), function () {
                frappe.prompt(
                    [
                        {
                            label: 'Seat Number',
                            fieldname: 'seat_number',
                            fieldtype: 'Data',
                            reqd: 1
                        }
                    ],
                    function (values) {
                        frm.set_value('seat', values.seat_number).then(() => {
                            frm.save();
                        });
                    },
                    ('Assign Seat'),
                    ('Assign')
                );
            }, ('Actions'));
        }
    },
});
// For license information, please see license.txt