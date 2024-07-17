class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor <= self.number_of_floors and new_floor > 0:

            for i in range(1, (new_floor + 1)):
                    print(i)
        else:
            print("Такого этажа не существует")


h1 = House("Кооператив 'Малина'", 7)
h2 = House("Кооператив'Клубника'", 15)


print(h1.name)
h1.go_to(8)
print(h2.name)
h2.go_to(9)


