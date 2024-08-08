class House:  # создание класса
    houses_history = []  # атрибут класса
    def __new__(cls, *args, **kwargs):  # переопределение класса
        cls.houses_history = cls.houses_history + [args[0]]  # добавление названия в список созданных объектов
        return super().__new__(cls)  # возврат вызова функции new
    def __init__(self, name, namber_of_floors):  # инициализация объекта
        self.name = name
        self.namber_of_floors = namber_of_floors
    def go_to(self, new_floor):  # определение метода перечисления этаже до целевого
        print(self.name)
        if new_floor > self.namber_of_floors:  # проверка на корректность целевого этажа
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):  # цикл перечисления этажей до целевого
                print(i)
    def __del__(self):  # переопределение метода del
        print(self.name, 'снесён, но он останется в истории')

print(House.houses_history)

h1 = House('ЖК Привилегия', 2)
h2 = House('ЖК Гравитация', 18)

print(h1)
print(h2)

print(House.houses_history)

del h1
del h2

print(House.houses_history)