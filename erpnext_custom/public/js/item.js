
frappe.ui.form.on("Item",{

	refresh: function (frm) {
		frm.add_custom_button(("Show All Work Order"), function(){
			// frappe.route_options = {
			//     from_warehouse : frm.doc.name
			// }, 
			frappe.set_route("List", "Stock Entry", {production_item : frm.doc.name})
		});
	},
})