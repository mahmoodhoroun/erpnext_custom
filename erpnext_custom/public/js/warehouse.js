
frappe.ui.form.on("Warehouse",{

	refresh: function (frm) {


		frm.add_custom_button(("Show Target Warehouse"), function(){
			console.log("fuck button")
			// frappe.route_options = {
			//     from_warehouse : frm.doc.name
			// }, 
			frappe.set_route("List", "Stock Entry", {from_warehouse : frm.doc.name})
		});
		frm.add_custom_button("Show Source Warehouse In Stock Entry", function(){
			frappe.set_route("List", "Stock Entry", {from_warehouse : frm.doc.name})
		})
	},
}

)