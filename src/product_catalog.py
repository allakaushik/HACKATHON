def get_product_catalog():
    return [
        {"id": 1, "name": "Shirt", "size": 40},
        {"id": 2, "name": "Jeans", "size": 30},
        {"id": 3, "name": "Jacket", "size": 40},
    ]


def select_product(product_id):
    catalog = get_product_catalog()
    for product in catalog:
        if product["id"] == product_id:
            return product
    return None
