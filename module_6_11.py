class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed
    def eat(self, food):
        if isinstance(food,Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
                print(f"{self.name} сыт")
            else:
                self.alive = False
                print(f"{self.name} съел {food.name}")
                print (f"{self.name} сдох")

class Plant:
    def __init__(self, name,edible = False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True



mumu = Mammal("Svin")
wolf = Predator("Volk")
rose = Flower("Myrose")
cacto = Fruit("Kaktus")


mumu.eat(rose)
wolf.eat(cacto)

print(mumu.alive)
print(mumu.fed)

print(wolf.alive)
print(wolf.fed)
