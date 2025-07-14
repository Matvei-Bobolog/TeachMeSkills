# =============================
# Домашняя работа: ООП на Python
# TeachMeSkills.by
# =============================

# Задание 1. Класс «Товар» и «Склад».
#
# Класс «Товар» содержит закрытые поля:
# - название товара
# - название магазина
# - стоимость в рублях
#
# Класс «Склад» содержит массив товаров.
#
# Обеспечить возможности:
# ✅ Вывод информации о товаре со склада по индексу
# ✅ Вывод информации о товаре со склада по имени
# ✅ Сортировка товаров по названию, по магазину и по цене
# ✅ Перегрузка сложения товаров по цене


class Product:
    def __init__(self, name, shop, price):
        self.name = name
        self.shop = shop
        self.price = price

    def __str__(self):
        return f"Название: {self.name}, магазин: {self.shop}, цена: {self.price}"

    def __add__(self, other):
        prices = self.price + other.price
        return prices


class Warehouse:
    def __init__(self):
        self.products = list()

    def add_product(self, product):
        self.products.append(product)

    def get_by_index(self, index):
        return self.products[index]

    def get_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product

    def sort_by_name(self):
        # TODO: отсортировать по названию
        self.products.sort(key = lambda product: product.name)

    def sort_by_shop(self):
        # TODO: отсортировать по магазину
        self.products.sort(key = lambda product: product.shop)

    def sort_by_price(self):
        # TODO: отсортировать по цене
        self.products.sort(key = lambda product: product.price)


# === Тесты для задачи 1 ===
print("=== Задача 1: Склад ===")
w = Warehouse()
p1 = Product("Молоко", "Пятерочка", 70)
p2 = Product("Хлеб", "Магнит", 40)
p3 = Product("Сыр", "Пятерочка", 300)

w.add_product(p1)
w.add_product(p2)
w.add_product(p3)

print(w.get_by_index(1))
print(w.get_by_name("Сыр"))

print("================= Изначальный список =================")
for product in w.products:
    print(product)

w.sort_by_name()

print("================= По названию =================")
for product in w.products:
    print(product)

w.sort_by_shop()

print("================= По магазину =================")
for product in w.products:
    print(product)

w.sort_by_price()

print("================= По цене =================")
for product in w.products:
    print(product)

print(p1 + p2)


# =============================
# Задание 2. Класс «ПчёлоСлон».
#
# Инициализируется двумя числами:
# - часть пчелы
# - часть слона
#
# Методы:
# ✅ Fly() – True, если часть пчелы >= части слона
# ✅ Trumpet() – "tu-tu-doo-doo", если часть слона >= пчелы, иначе "wzzzz"
# ✅ Eat(meal, value) – meal только "nectar" или "grass".
#   - если nectar: у слона уменьшается, у пчелы увеличивается
#   - если grass: наоборот
#   - нельзя выйти за пределы 0–100


class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def fly(self):
        return self.bee_part >= self.elephant_part

    def trumpet(self):
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo"
        return "wzzzz"

    def eat(self, meal, value):
        value = max(min(value, 100), 0)
        if meal == "nectar":
            self.elephant_part -= value
            self.bee_part += value
        elif meal == "grass":
            self.elephant_part += value
            self.bee_part -= value
        else:
            pass


# === Тесты для задачи 2 ===
print("\n=== Задача 2: ПчёлоСлон ===")
be = BeeElephant(30, 70)
print(be.fly())            # False
print(be.trumpet())        # tu-tu-doo-doo
be.eat("nectar", 20)       # должно изменить пропорции
print(be.fly())            # возможно True


# =============================
# Задание 3. Класс «Автобус».
#
# Свойства:
# ✅ скорость
# ✅ макс. кол-во мест
# ✅ макс. скорость
# ✅ список фамилий пассажиров
# ✅ флаг наличия свободных мест
# ✅ словарь мест (номер: фамилия)
#
# Методы:
# ✅ посадка/высадка одного или нескольких пассажиров
# ✅ увеличение/уменьшение скорости на заданное значение
# ✅ операции:
#   - `in` проверяет фамилию в списке
#   - `+=` посадка
#   - `-=` высадка


# === TODO: реализовать класс Bus ===
class Bus:
    def __init__(self, max_seats, max_speed):
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []

    @property
    def not_full(self):
        return self.max_seats > len(self.passengers)
    
    @property
    def seats_dict(self):
        seats_dict = dict()
        for i in range(self.max_seats):
            try:
                seats_dict[i] = self.passengers[i]
            except IndexError:
                seats_dict[i] = "empty"
        return seats_dict

    def board(self, *passengers):
        for passenger in passengers:
            self.passengers.append(passenger)

    def unboard(self, *passengers):
        for passenger in passengers:
            self.passengers.remove(passenger)

    def change_speed(self, delta):
        self.max_speed += delta

    def __contains__(self, surname):
        return surname in self.passengers

    def __iadd__(self, surname):
        self.passengers.append(surname)
        return self

    def __isub__(self, surname):
        self.passengers.remove(surname)
        return self


# === Тесты для задачи 3 ===
print("\n=== Задача 3: Автобус ===")
bus = Bus(max_seats=3, max_speed=100)
bus.board("Иванов", "Петров")
print("Иванов" in bus)     # True
bus += "Сидоров"
print("Сидоров" in bus)    # True
bus -= "Петров"
print("Петров" in bus)     # False
bus.change_speed(20)