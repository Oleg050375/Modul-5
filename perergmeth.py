class House:  # создание класса
    def __init__(self, name, namber_of_floors):  # инициализация класса
        self.name = name
        self.namber_of_floors = namber_of_floors
        if isinstance(self.namber_of_floors, int):
            pass
        else:
            print(self.name, '- неверный формат задания этажности')
    def go_to(self, new_floor):  # определение метода перечисления этаже до целевого
        print(self.name)
        if new_floor > self.namber_of_floors:  # проверка на корректность целевого этажа
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):  # цикл перечисления этажей до целевого
                print(i)
    def __len__(self):  # определение метода на случай применения оператора len
        return self.namber_of_floors
    def __str__(self):  # определение метода на случай применения оператолра str
        return 'Название: ' + self.name + ', ' + 'количество этажей: ' + str(self.namber_of_floors)
    def __eq__(self, other):  # ==
        if isinstance(other.namber_of_floors, int) and isinstance(self.namber_of_floors, int):
            return self.namber_of_floors == other.namber_of_floors
        return ('Неверный формат этажности')
    def __lt__(self, other):  # <
        if isinstance(other.namber_of_floors, int) and isinstance(self.namber_of_floors, int):
            return self.namber_of_floors < other.namber_of_floors
        return ('Неверный формат этажности')
    def __le__(self, other):  # <=
        if isinstance(other.namber_of_floors, int) and isinstance(self.namber_of_floors, int):
            return self.namber_of_floors <= other.namber_of_floors
        return ('Неверный формат этажности')
    def __gt__(self, other):  # >
        if isinstance(other.namber_of_floors, int) and isinstance(self.namber_of_floors, int):
            return self.namber_of_floors > other.namber_of_floors
        return ('Неверный формат этажности')
    def __ge__(self, other):  # >=
        if isinstance(other.namber_of_floors, int) and isinstance(self.namber_of_floors, int):
            return self.namber_of_floors >= other.namber_of_floors
        return ('Неверный формат этажности')
    def __ne__(self, other):  # !=
        if isinstance(other.namber_of_floors, int) and isinstance(self.namber_of_floors, int):
            return self.namber_of_floors != other.namber_of_floors
        return ('Неверный формат этажности')
    def __add__(self, value):  # +
        if isinstance(value, int) and isinstance(self.namber_of_floors, int):
            self.namber_of_floors = self.namber_of_floors + value
            return self
        return ('Неверный формат данных')
    def __iadd__(self, value): # +=
        if isinstance(value, int) and isinstance(self.namber_of_floors, int):
            self.namber_of_floors = self.namber_of_floors + value
            return self
        return ('Неверный формат данных')
    def __radd__(self, value):
        if isinstance(value, int) and isinstance(self.namber_of_floors, int):
            self.namber_of_floors = self.namber_of_floors + value
            return self
        return ('Неверный формат данных')

h1 = House('ЖК Привилегия', 2)
h2 = House('ЖК Гравитация', 18)

print(h1)
print(h2)
print('==', h1 == h2)
print('<', h1 < h2)
print('<=', h1 <= h2)
print('>', h1 > h2)
print('>=', h1 >= h2)
print('!=', h1 != h2)
print(h1 + 10)
h1 += 5
print(h1)
h1 = 20 + h1
print(h1)