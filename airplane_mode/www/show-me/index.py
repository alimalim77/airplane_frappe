import frappe

def get_context(context):
    # Get the query parameter as string first
    color_str = frappe.form_dict.get('color', 'red')  # default to 'red' if not provided
    context.title = "Hello World"
    context.color = color_str

    return context
