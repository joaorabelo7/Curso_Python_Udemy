product = {
    'name': 'Blue Pen',
    'price': 2.5,
    'category': 'desk',
}

dc ={
    key : value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
}

print(dc)