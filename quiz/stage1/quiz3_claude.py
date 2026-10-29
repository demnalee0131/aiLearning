import math


class Shape:
    """Base class for shapes: defines the interface only, no concrete implementation"""
    
    def __init__(self, name):
        self.name = name # Attribute shared by all shapes

    def area(self):
        raise NotImplementedError("子类必须实现 area() 方法")
    

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle") # Call the base constructor to set name
        self.width = width
        self.height = height

    def area(self): # Override the base class method
        return self.width * self.height
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle") # Call the base class constructor to set name
        self.radius = radius

    def area(self): # Override the base class method
        return math.pi * self.radius ** 2

if __name__ == "__main__":
    shapes = [Rectangle(3, 4), Circle(1), Rectangle(5, 2), Circle(2.5)]

    # Polymorphism: the same area() call runs each object's own implementation
    for s in shapes:
        print(f"{s.name:<10} 面积 = {s.area():.2f}")

    # Demo: calling area() on the base class directly raises an error
    try:
        Shape("Shape").area()
    except NotImplementedError as e:
        print("调用 Shape().area() ->", e)