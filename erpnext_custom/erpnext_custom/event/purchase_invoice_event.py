import frappe
@frappe.whitelist()
def create_purchase_receipt(doc, event):
    purchase_receipt_doc = frappe.new_doc("Purchase Receipt")
    purchase_receipt_doc.supplier = doc.supplier
    for purchase_invoice_item in doc.items:
        purchase_receipt_doc.append("items",{"item_code": purchase_invoice_item.item_code, "received_qty": purchase_invoice_item.qty})

    purchase_receipt_doc.insert(ignore_permissions=True)