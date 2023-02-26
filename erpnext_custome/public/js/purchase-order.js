frappe.ui.form.on("Purchase Order", {
	setup: function(frm) {

		frm.set_query("suppliertest", function() {
			return {
				filters: {
					"supplier_type": "company",
				}
			}
		});
    }
}
)
    
        