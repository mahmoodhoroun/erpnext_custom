import frappe

def validate_add_custom_remarks(doc, method):
    if doc.note:
        note = doc.note
        doc.remarks = note

def validate_payments_sales_invoice(doc, method):
    # frappe.throw("nvfvidkn")
    if doc.is_pos:
        for payment in doc.get("payments"):
            print(payment.amount)
            if payment.amount == 0:
                frappe.throw("not allow any  payments with 0 ")
    