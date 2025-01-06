from Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Сторона должна быть больше 0")

        elif (
            side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("Данная фигура не является треугольником")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.s = (
            side_a + side_b + side_c
        ) / 2  # Вычисление полупериметра для формулы Герона

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        return math.sqrt(
            self.s
            * (self.s - self.side_a)
            * (self.s - self.side_b)
            * (self.s - self.side_c)
        )
