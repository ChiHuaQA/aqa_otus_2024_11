from Figure import Figure
from Square import Square
from Triangle import Triangle
from Rectangle import Rectangle
import math


class Circle(Figure):
    def __init__(self, radius: int | float):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше 0")
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return self.perimeter * math.pi


c = Circle(radius=3)
s = Square(6)
r = Rectangle(side_a=3, side_b=5)
t = Triangle(side_a=5, side_b=6, side_c=7)

print(c.add_area(r))
