from . import __version__ as app_version

app_name = "pibicut_invoice"
app_title = "Pibicut Invoice"
app_publisher = "PibiCo"
app_description = "TLV QRCode for E-Invoices"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pibico.sl@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pibicut_invoice/css/pibicut_invoice.css"
# app_include_js = "/assets/pibicut_invoice/js/pibicut_invoice.js"

# include js, css files in header of web template
# web_include_css = "/assets/pibicut_invoice/css/pibicut_invoice.css"
# web_include_js = "/assets/pibicut_invoice/js/pibicut_invoice.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pibicut_invoice/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# before_install = "pibicut_invoice.install.before_install"
# after_install = "pibicut_invoice.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pibicut_invoice.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
  "Sales Invoice": {
    "before_save": "pibicut_invoice.pibicut_invoice.custom.generate_tlv_qr",
    "after_submit": "pibicut_invoice.pibicut_invoice.custom.generate_tlv_qr"
  },
  "POS Invoice": {
    "before_save": "pibicut_invoice.pibicut_invoice.custom.generate_tlv_qr",
    "after_submit": "pibicut_invoice.pibicut_invoice.custom.generate_tlv_qr"
  }
   #"*": {
 	#	"on_update": "method",
 	#	"on_cancel": "method",
 	#	"on_trash": "method"
	#}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pibicut_invoice.tasks.all"
# 	],
# 	"daily": [
# 		"pibicut_invoice.tasks.daily"
# 	],
# 	"hourly": [
# 		"pibicut_invoice.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pibicut_invoice.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pibicut_invoice.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pibicut_invoice.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pibicut_invoice.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pibicut_invoice.task.get_dashboard_data"
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
# 	"pibicut_invoice.auth.validate"
# ]

fixtures = ["Property Setter", {"doctype": "Custom Field", "filters": [ ["dt", "in", ("Sales Invoice", "Company", "POS Invoice")] ]}, {"doctype": "Client Script", "filters": [ ["dt", "in", ("Sales Invoice", "POS Invoice")] ]}, {"doctype": "Print Format", "filters": [ ["doc_type", "in", ("Sales Invoice", "POS Invoice")] ]}]