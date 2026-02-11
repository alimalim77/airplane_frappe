import frappe

def get_context(context):
    shop_name = frappe.form_dict.shop
    if not shop_name:
        frappe.throw("Shop not specified", frappe.DoesNotExistError)

    context.shop = frappe.get_doc("Airport Shop", shop_name)
    context.no_cache = 1
