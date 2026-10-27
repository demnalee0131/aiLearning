# 2-1

class Dog:
    species = "canine"
    def __init__(self, name):
        self.name = name

a, b = Dog("A"), Dog("B")
Dog.species = "wolf"
print(a.species)
a.species = "cat"
print(a.species, b.species)
print(a.__dict__)