class Dish:
    """Клас, що представляє страву в меню."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} - {self.price} грн"


class Menu:
    """Клас, що представляє меню ресторану."""
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish: Dish):
        """Додає страву до меню."""
        self.dishes.append(dish)

    def remove_dish(self, dish_name: str):
        """Видаляє страву з меню за її назвою."""
        self.dishes = [dish for dish in self.dishes if dish.name != dish_name]

    def update_dish_price(self, dish_name: str, new_price: float):
        """Оновлює ціну страви в меню."""
        for dish in self.dishes:
            if dish.name == dish_name:
                dish.price = new_price
                break

    def get_dishes(self):
        """Повертає список страв."""
        return self.dishes


class Order:
    """Клас, що представляє замовлення."""
    def __init__(self, client, dishes):
        self.client = client
        self.dishes = dishes

    def get_total_price(self):
        """Обчислює загальну вартість замовлення."""
        return sum(dish.price for dish in self.dishes)

    def add_dish(self, dish: Dish):
        """Додає нову страву до замовлення."""
        self.dishes.append(dish)

    def remove_dish(self, dish_name: str):
        """Видаляє страву з замовлення за її назвою."""
        self.dishes = [dish for dish in self.dishes if dish.name != dish_name]

    def __repr__(self):
        dishes_list = ", ".join([dish.name for dish in self.dishes])
        return f"Замовлення для {self.client}: {dishes_list} на {self.get_total_price()} грн"


class OrderDatabase:
    """Singleton-клас для збереження замовлень."""
    _instance = None
    _orders = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderDatabase, cls).__new__(cls)
        return cls._instance

    def add_order(self, order):
        """Додає замовлення в базу."""
        self._orders.append(order)

    def get_orders(self):
        """Повертає всі замовлення."""
        return self._orders

    def filter_orders_by_client(self, client_name):
        """Фільтрує замовлення за клієнтом."""
        return [order for order in self._orders if order.client == client_name]

    def filter_orders_by_price(self, min_price, max_price):
        """Фільтрує замовлення за ціною."""
        return [order for order in self._orders if min_price <= order.get_total_price() <= max_price]


class KitchenNotifier:
    """Оповіщувач кухні про нове замовлення."""
    def notify(self, order):
        print(f"🔔 Кухня отримала нове замовлення: {order}")


class OrderFactory:
    """Фабрика для створення замовлень."""
    @staticmethod
    def create_order(order_type, client, dishes):
        if order_type == "regular":
            return Order(client, dishes)
        else:
            raise ValueError("❌ Невідомий тип замовлення!")


# Приклад використання
menu = Menu()
menu.add_dish(Dish("Салат", 50))
menu.add_dish(Dish("Суп", 40))

order1 = Order("Олександр", [menu.dishes[0]])
order2 = Order("Марія", [menu.dishes[1]])

order_db = OrderDatabase()
order_db.add_order(order1)
order_db.add_order(order2)

print(order_db.get_orders())  # Показує всі замовлення

# Фільтруємо за клієнтом
print(order_db.filter_orders_by_client("Олександр"))

# Оновлюємо страву в меню
menu.update_dish_price("Салат", 55)

# Додаємо страви до замовлення
order1.add_dish(menu.dishes[1])

# Видаляємо страви з замовлення
order2.remove_dish("Суп")

# Повідомлення на кухню
notifier = KitchenNotifier()
notifier.notify(order1)
