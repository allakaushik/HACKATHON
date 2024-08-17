from ar_simulation import virtual_try_on
from product_catalog import get_product_catalog, select_product
from logistics import select_delivery_option


def main():
    print("Welcome to AR-Powered Virtual Shopping Assistant")

    catalog = get_product_catalog()
    print("Product Catalog:")
    for product in catalog:
        print(f"{product['id']}. {product['name']} (Size: {product['size']})")

    product_id = int(input("Enter the Product ID to try on: "))
    product = select_product(product_id)
    if not product:
        print("Invalid Product ID")
        return

    user_size = int(input("Enter your size: "))
    fit_message = virtual_try_on(user_size, product)
    print(fit_message)

    print("1. Pickup at mall\n2. Home delivery")
    delivery_option = int(input("Select delivery option: "))
    delivery_message = select_delivery_option(delivery_option)
    print(delivery_message)


if __name__ == "__main__":
    main()
