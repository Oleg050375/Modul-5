class House:  # создание класса
    def __init__(self, name, namber_of_floors):  # инициализация класса
        self.name = name
        self.namber_of_floors = namber_of_floors
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

h1 = House('ЖК Привилегия', 2)
h2 = House('ЖК Гравитация', 18)

# h1.go_to(3)
# h2.go_to(5)

print(len(h1))
print(len(h2))

print(str(h1))
print(str(h2))