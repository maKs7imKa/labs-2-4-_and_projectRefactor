import pytest
from constructor import User, Product, OrderItem, Order, ShoppingCart

@pytest.fixture
def setup_data():
    user = User(1, "Jec Doe", "jec@gmail.com")
    product1 = Product(1, "Laptop", 1000.0, 10)
    product2 = Product(2, "Phone", 500.0, 20)
    cart = ShoppingCart(user)
    return user, product1, product2, cart

# Тест реєстрації користувача
def test_register(setup_data):
    user, _, _, _ = setup_data
    user.register()
    assert user.name == "Jec Doe"
    assert user.email == "jec@gmail.com"

# Тест додавання продукту в кошик
def test_add_product_to_cart(setup_data):
    user, product1, _, cart = setup_data
    cart.add_product(product1, 2)
    assert len(cart.items) == 1
    assert cart.items[0].product == product1
    assert cart.items[0].quantity == 2

# Тест додавання кількох продуктів в кошик
def test_add_multiple_products_to_cart(setup_data):
    user, product1, product2, cart = setup_data
    cart.add_product(product1, 2)
    cart.add_product(product2, 1)
    assert len(cart.items) == 2
    assert cart.items[1].product == product2
    assert cart.items[1].quantity == 1

# Тест оформлення замовлення
def test_checkout(setup_data):
    user, product1, _, cart = setup_data
    cart.add_product(product1, 2)
    order = cart.checkout()
    assert len(order.items) == 1
    assert order.items[0].quantity == 2
    assert order.user == user

# Тест підрахунку загальної вартості замовлення
def test_order_total(setup_data):
    user, product1, _, _ = setup_data
    order = Order(1, user)
    order.add_item(product1, 2)
    order.add_item(product1, 3)
    total = order.calculate_total()
    assert total == 5000.0  # 2 * 1000 + 3 * 1000

# Тест видалення товару з кошика
def test_remove_product_from_cart(setup_data):
    user, product1, _, cart = setup_data
    cart.add_product(product1, 2)
    cart.remove_product(product1)
    assert len(cart.items) == 0

# Тест правильності підрахунку вартості одного товару
def test_order_item_total_price(setup_data):
    _, product1, _, _ = setup_data
    order_item = OrderItem(product1, 3)
    total_price = order_item.get_total_price()
    assert total_price == 3000.0  # 3 * 1000

# Тест на перевірку коректного створення кількох замовлень користувачем
def test_multiple_orders(setup_data):
    user, product1, _, cart = setup_data
    cart.add_product(product1, 2)
    order1 = cart.checkout()
    cart.add_product(product1, 1)
    order2 = cart.checkout()
    assert len(user.orders) == 2
    assert order1 != order2

# Тест, що перевіряє, чи не можна оформити замовлення без товарів
def test_checkout_empty_cart(setup_data):
    user, _, _, cart = setup_data
    order = cart.checkout()
    assert len(order.items) == 0
    assert order.status == "Pending"

# Тест на правильність відображення продукту в замовленні
def test_order_contains_correct_product(setup_data):
    user, product1, _, cart = setup_data
    cart.add_product(product1, 2)
    order = cart.checkout()
    assert order.items[0].product.name == "Laptop"
    assert order.items[0].quantity == 2
