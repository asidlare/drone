from math import sqrt


class PositiveInt:
    # Overriding the __new__ method
    def __new__(cls, *args, **kwargs):
        for value in (*args, *list(kwargs.values())):
            if not (isinstance(value, int) and value > 0):
                # Raising a ValueError if the attribute is not an integer
                raise ValueError("Attribute is not a positive integer")
        return super().__new__(cls)


class CircleUtils:
    @staticmethod
    def distance(x1: int, y1: int, x2: int, y2: int) -> float:
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    @staticmethod
    def r_sum(r1: int, r2: int) -> float:
        return float(r1 + r2)

    @staticmethod
    def r_diff(r1: int, r2: int) -> float:
        return float(abs(r1 - r2))

    @staticmethod
    def point_belongs_to_circle(x: int, y: int, r: int, x_point: int, y_point: int) -> bool:
        return sqrt((x_point - x) ** 2 + (y_point - y) ** 2) <= float(r)
