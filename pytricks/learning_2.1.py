# asserts
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], 'Invalid discount!!'
    return price


product_details = {'price': 1000, 'name': 'bottle'}
print(apply_discount(product_details, 1.2))
print(__debug__)  # True by default but while optimization(python3.9 -O pytricks/test.py) it will be False

# Complacent comma placement
li = [
    '1',
    '2',
    '3',
    '4',  # always place comma after set, dict and list
]
print(li)
