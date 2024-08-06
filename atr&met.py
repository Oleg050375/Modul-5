class House:
    def __init__(self, name, namber_of_floors):
        self.name = name
        self.namber_of_floors = namber_of_floors
    def go_to(self, new_floor):
        print(self.name)
        if new_floor > self.namber_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('ЖК Привилегия', 2)
h2 = House('ЖК Гравитация', 18)

h1.go_to(3)
h2.go_to(5)
