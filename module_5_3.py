class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors} "
    def __eq__(self, other):  # ==
        return self.number_of_floors == other.nomber_of_floors
    def __lt__(self, other): # <
        return self.number_of_floors < other.number_of_floors
    def __le__ (self, other):  # <=
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other): # >
        return self.number_of_floors > other.number_of_floors
    def __ge__ (self, other):  # >=
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other): #!=
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value): #+
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self



h1 = House("Кооператив 'Малина'", 7)
h2 = House("Кооператив'Клубника'", 15)

print(h1)
print(h2)
print(len(h1))
print(len(h2))
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 + "n")
print(h1 + 3)
print(2.3 + h1)
print(2 + h1)
print(h2 + 5)

