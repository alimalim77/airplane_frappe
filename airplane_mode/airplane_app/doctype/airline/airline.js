frappe.ui.form.on("Airline", {
	refresh(frm) {


		if (frm.doc.website) {
            // Wait for sidebar to render
            setTimeout(() => {
                let sidebar = document.querySelector('.layout-side-section');
                if (sidebar && !sidebar.querySelector('.custom-visit-website')) {
                    let btn = document.createElement('a');
                    btn.href = frm.doc.website;
                    btn.target = '_blank';
                    btn.innerText = 'Visit Website';
                    btn.className = 'btn btn-primary custom-visit-website';
                    btn.style.display = 'block';
                    btn.style.marginBottom = '10px';
                    sidebar.prepend(btn);
                }
            }, 300);
        }
	}
});