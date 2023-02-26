import frappe 

@frappe.whitelist()
def validate_add_note_toremarksss(doc, method):
    itemss = ""
    for item in doc.get("items"):
        itemss += item.note
        
    doc.remarks = str(itemss)

@frappe.whitelist()
def validate_payment_is_pos(doc , method):
    if doc.is_pos:
        for pay in doc.get("payments"):
            if pay.amount <= 0:
                 frappe.throw("Your Payment Amount Can not be zero Because you make sales invoice (is pos) ")


@frappe.whitelist()
def get_customer(customer):
    customers = frappe.db.sql(f""" SELECT * from `tabCustomer` Where name = {customer} """)
    return customers;