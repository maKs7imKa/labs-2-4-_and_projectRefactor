import pytest
import pylint
from constructor import Dish, Menu, Order, OrderDatabase, OrderFactory, KitchenNotifier


# ✅ Тест 1: Додавання страви до меню
def test_add_dish_to_menu():
    menu = Menu()
    pizza = Dish("Pizza", 150)
    menu.add_dish(pizza)
    assert pizza in menu.get_dishes()


# ✅ Тест 2: Підрахунок загальної вартості замовлення
def test_order_total_price():
    pizza = Dish("Pizza", 150)
    sushi = Dish("Sushi", 200)
    order = Order("Іван", [pizza, sushi])
    assert order.get_total_price() == 350


# ✅ Тест 3: Singleton працює правильно
def test_singleton_order_database():
    db1 = OrderDatabase()
    db2 = OrderDatabase()
    assert db1 is db2  # Обидва екземпляри повинні вказувати на один об'єкт


# ✅ Тест 4: Фабрика створює замовлення
def test_factory_creates_order():
    pizza = Dish("Pizza", 150)
    order = OrderFactory.create_order("regular", "Іван", [pizza])
    assert isinstance(order, Order)


# ✅ Тест 5: Оповіщувач кухні працює
def test_kitchen_notifier(capsys):
    pizza = Dish("Pizza", 150)
    order = Order("Іван", [pizza])
    notifier = KitchenNotifier()
    notifier.notify(order)

    captured = capsys.readouterr()
    assert "Кухня отримала нове замовлення" in captured.out


# ✅ Тест 6: Коректне представлення страви
def test_dish_repr():
    dish = Dish("Burger", 120)
    assert repr(dish) == "Burger - 120 грн"


# ✅ Тест 7: Додавання кількох замовлень до бази
def test_add_multiple_orders():
    db = OrderDatabase()
    db._orders = []  # Очистка перед тестом
    order1 = Order("Олег", [Dish("Pasta", 180)])
    order2 = Order("Марина", [Dish("Soup", 90)])
    db.add_order(order1)
    db.add_order(order2)

    # Перевірка кількості замовлень
    assert len(db.get_orders()) == 2
    # Перевірка правильності замовлень
    assert db.get_orders()[0].client == "Олег"
    assert db.get_orders()[1].client == "Марина"


# ✅ Тест 8: Фабрика не створює невідомий тип замовлення
def test_invalid_order_type():
    with pytest.raises(ValueError):
        OrderFactory.create_order("unknown", "Іван", [])


# ✅ Тест 9: Замовлення без страв має нульову ціну
def test_empty_order_price():
    order = Order("Іван", [])
    assert order.get_total_price() == 0
    assert len(order.dishes) == 0  # Перевірка, що страви справді відсутні


# ✅ Тест 10: Отримання списку страв із меню
def test_get_menu_items():
    menu = Menu()
    pasta = Dish("Pasta", 180)
    soup = Dish("Soup", 90)
    menu.add_dish(pasta)
    menu.add_dish(soup)
    assert menu.get_dishes() == [pasta, soup]

    # Перевірка на порожнє меню
    empty_menu = Menu()
    assert empty_menu.get_dishes() == []


# python -m pytest -v test_app.py
# python -m pylint -v test_app.py