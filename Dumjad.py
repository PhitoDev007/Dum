from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        pass
    
    def fact(self):
        return "I am a two-dimensional shape."
    
    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    
    def area(self):
        return self.length**2
    
    def fact(self):
        return "Squares have each angle equal to 90 degrees."

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return pi*self.radius**2

class EquilateralTriangle(Shape):
    def __init__(self, baseLength):
        super().__init__("Equilateral Triangle")
        self.baseLength = baseLength
    
    def area(self):
        return (self.baseLength**2 * (3**0.5)) / 4
    
    def fact(self):
        return "An equilateral triangle has equal sides on each side"

class AnyTriangle(Shape):
    def __init__(self, baseLength, height):
        super().__init__("Any Triangle")
        self.baseLength = baseLength
        self.height = height
    
    def area(self):
        return 0.5 * self.baseLength * self.height
    
    def fact(self):
        return "A triangle has three sides"

a = Square(4)
b = Circle(7)
c = EquilateralTriangle(5)
d = AnyTriangle(6, 8)

for anyShape in (a, b, c, d):
    print(anyShape)
    print(anyShape.area())
    print(anyShape.fact())