def virtual_try_on(size, product):
    if size == product["size"]:
        return f"The {product['name']} fits you perfectly!"
    else:
        return f"The {product['name']} might be too {'small' if size < product['size'] else 'large'} for you."
