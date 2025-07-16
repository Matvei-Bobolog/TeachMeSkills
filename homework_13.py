# ================================
# TeachMeSkills.by — Домашнее задание
# ================================
"""
Здесь задания на генераторы и паттерны проектирования:
- Строитель
- Фабричный метод
- Стратегия

Заполняйте TODO, читайте комментарии и запускайте тесты.
"""

# ================================
# ЗАДАНИЕ 1: Генератор чисел Фибоначчи
# ================================

def fibonacci_generator(n: int):
    """Генераторная функция, возвращает n чисел Фибоначчи."""
    f = 0
    p = 1
    for _ in range(n):
        yield p
        f, p = p, f + p

# Тест:
print("\n--- Задание 1 ---")
n = int(input("Сколько чисел Фибоначчи вывести? "))
for num in fibonacci_generator(n):
    print(num, end=' ')
print()


# ================================
# ЗАДАНИЕ 2: Бесконечная циклическая последовательность
# ================================

def cycle_123():
    """Генераторная функция, бесконечно выдаёт 1-2-3"""
    while True:
        for i in range(1, 4):
            yield i

# Тест:
print("\n--- Задание 2 ---")
count = int(input("Сколько чисел вывести из бесконечного цикла? "))
gen = cycle_123()
for _ in range(count):
    print(next(gen), end=' ')
print()


# ================================
# ЗАДАНИЕ 3: Паттерн «Строитель»
# ================================

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon})"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size

    def add_cheese(self):
        self.pizza.cheese = True
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True

    def add_mushrooms(self):
        self.pizza.mushrooms = True

    def add_onions(self):
        self.pizza.onions = True

    def add_bacon(self):
        self.pizza.bacon = True
    
    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self):
        self.builder.set_size(80)
        self.builder.add_cheese()
        self.builder.add_mushrooms()
        return self.builder.build()


# Тест:
print("\n--- Задание 3 ---")
builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)


# ================================
# ЗАДАНИЕ 4: Паттерн «Фабричный метод»
# ================================

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("woof")


class Cat(Animal):
    def speak(self):
        print("meow")


class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()


# Тест:
print("\n--- Задание 4 ---")
factory = AnimalFactory()
animal = factory.create_animal("dog")
animal.speak()
animal = factory.create_animal("cat")
animal.speak()


# ================================
# ЗАДАНИЕ 5: Паттерн «Стратегия»
# ================================

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(OperationStrategy):
    def execute(self, a, b):
        return a + b


class Subtraction(OperationStrategy):
    def execute(self, a, b):
        return a - b


class Multiplication(OperationStrategy):
    def execute(self, a, b):
        return a * b


class Division(OperationStrategy):
    def execute(self, a, b):
        return a / b


class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)


# Тест:
print("\n--- Задание 5 ---")
calc = Calculator()
calc.set_strategy(Addition())
print("5 + 3 =", calc.calculate(5, 3))
calc.set_strategy(Subtraction())
print("5 - 3 =", calc.calculate(5, 3))
calc.set_strategy(Multiplication())
print("5 * 3 =", calc.calculate(5, 3))
calc.set_strategy(Division())
print("5 / 3 =", calc.calculate(5, 3))


# ================================
# УДАЧИ! 🚀
# ================================