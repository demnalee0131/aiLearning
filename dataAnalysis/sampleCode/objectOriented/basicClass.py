class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

d = Dog("Rex", 3)
print(d.bark())
print(Dog.bark(d))