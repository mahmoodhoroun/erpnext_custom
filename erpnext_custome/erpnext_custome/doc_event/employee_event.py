import frappe

# def validate_reason_for_leaving(doc , event):
# 		if doc.status == "Left":
# 			if not doc.reason_for_leaving:
# 				frappe.throw("must enter reason for leaving")

def create_task(doc , event):
    #create new Task for employee on validate
    if doc.status == "Left":
        task = frappe.new_doc("Task")
        task.subject = "End Of service" + str(doc.employee_name)
        task.insert()
        