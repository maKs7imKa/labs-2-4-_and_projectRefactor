class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def register(self):
        print(f"User {self.name} registered.")

    def login(self):
        print(f"User {self.name} logged in.")

    def view_orders(self):
        return self.orders


class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


class Order:
    def __init__(self, order_id: int, user: User):
        self.order_id = order_id
        self.user = user
        self.items = []
        self.status = "Pending"

    def add_item(self, product: Product, quantity: int):
        self.items.append(OrderItem(product, quantity))

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)


class ShoppingCart:
    def __init__(self, user: User):
        self.user = user
        self.items = []

    def add_product(self, product: Product, quantity: int):
        self.items.append(OrderItem(product, quantity))

    def remove_product(self, product: Product):
        self.items = [item for item in self.items if item.product != product]

    def checkout(self):
        new_order = Order(len(self.user.orders) + 1, self.user)
        new_order.items = self.items
        self.user.orders.append(new_order)
        self.items = []
        return new_order
