// Copyright (c) 2025, alim and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
	refresh(frm) {
		frappe.realtime.on("gate_updated", (data) => {
			if (data.flight === frm.doc.name) {
				frappe.msgprint(__("Gate updated to {0} for all tickets!", [data.gate]));
				frm.reload_doc();
			}
		});
	},
});
