import frappe
@frappe.whitelist()
def create_stock_entry(doc, event):
    # frappe.msgprint("mdksgnsdljghu")

    if(doc.material_request_type == "Material Transfer" and doc.set_from_warehouse and doc.set_warehouse):
        stock_entry_doc = frappe.new_doc("Stock Entry")
        stock_entry_doc.stock_entry_type = doc.material_request_type
        stock_entry_doc.from_warehouse = doc.set_from_warehouse
        for item in doc.get("items"):
            stock_entry_doc.append("items",{"s_warehouse":item.from_warehouse, 
                                            "t_warehouse": item.warehouse,
                                            "qty": item.qty,
                                            })
                

        stock_entry_doc.insert()


    