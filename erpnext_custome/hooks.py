from . import __version__ as app_version

app_name = "erpnext_custome"
app_title = "Erpnext Custome"
app_publisher = "husam hammad"
app_description = "Erpnext Custome App"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "huasmhammad542@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_custome/css/erpnext_custome.css"
# app_include_js = "/assets/erpnext_custome/js/erpnext_custome.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_custome/css/erpnext_custome.css"
# web_include_js = "/assets/erpnext_custome/js/erpnext_custome.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_custome/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {"Purchase Order" : "public/js/purchase-order.js",
              "Quotation": "public/js/quotation.js",
              "Sales Invoice" : "public/js/sales_invoice.js"
              }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_custome.install.before_install"
# after_install = "erpnext_custome.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpnext_custome.uninstall.before_uninstall"
# after_uninstall = "erpnext_custome.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_custome.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Purchase Order": "erpnext_custome.erpnext_custome.overrides.purchase_order.PurchaseOrder"
}

# Document Events
# --------------
# Hook on document methods and events

doc_events = {
	"Employee": {
		# "validate": "erpnext_custome.erpnext_custome.doc_event.employee_event.validate_reason_for_leaving",
		"validate": "erpnext_custome.erpnext_custome.doc_event.employee_event.create_task",	},
    "Attendance": {
        "validate": "erpnext_custome.erpnext_custome.doc_event.attendance_event.clac_hours",
	},
    "Sales Invoice": {
		"validate":"erpnext_custome.erpnext_custome.doc_event.sales_invoice_event.validate_add_note_toremarksss",
        "validate":"erpnext_custome.erpnext_custome.doc_event.sales_invoice_event.validate_payment_is_pos",
        } 
    
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"erpnext_custome.tasks.all"
#	],
#	"daily": [
#		"erpnext_custome.tasks.daily"
#	],
#	"hourly": [
#		"erpnext_custome.tasks.hourly"
#	],
#	"weekly": [
#		"erpnext_custome.tasks.weekly"
#	]
#	"monthly": [
#		"erpnext_custome.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "erpnext_custome.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "erpnext_custome.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "erpnext_custome.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"erpnext_custome.auth.validate"
# ]

