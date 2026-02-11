import frappe

def get_context(context):
    context.shops = frappe.get_all(
        "Airport Shop",
        fields=[
            "name", "name1", "shop_number", "airport",
            "tenant_name", "area_of_shop", "select_pnxu",
            "rent_amount"
        ],
        order_by="shop_number asc"
    )
    context.no_cache = 1
