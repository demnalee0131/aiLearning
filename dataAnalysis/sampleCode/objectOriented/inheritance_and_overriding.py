# 3-1

class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 100
    def speak(self):
        return "..."

class Cat(Animal):
    def __init__(self, name, indoor):
        super().__init__(name)
        self.indoor = indoor

    def speak(self):
        return f"{self.name}: meow"

c = Cat("Tom", True)
print(c.speak(), c.energy)

# If remove super().__init__(), c.energy will raise an AttributeError because 
# the `energy` attribute is not initialized.