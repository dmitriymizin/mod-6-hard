import math

class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        if self.sides_count == 1:
            perimetr = self.__sides[0]
        else:
            for side in self.__sides:
                perimetr += side
        return perimetr

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *sides):
        if len(sides) == self.sides_count:
            super().__init__(__color, sides)
            self.__radius = sides[0] / (2 * 3.14)
        else:
            super().__init__(__color, [1] * self.sides_count)
            self.__radius = 1 / (2 * 3.14)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        s = 3.14 * (self.__radius ** 2)
        return s

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *sides):
        if len(sides) == self.sides_count:
            super().__init__(__color, sides)
        else:
            super().__init__(__color, [1] * self.sides_count)

    def checking_for_triangularity(self):
        side1, side2, side3 = self.get_sides()
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            return True
        else:
            print('Такие значения не могут образовывать треугольник')
            return False

    def get_square(self):
        if self.checking_for_triangularity():
            side1, side2, side3 = self.get_sides()
            p = sum(self.get_sides()) / 2
            s = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
            return s
        else:
            print('Площадь не может быть рассчитана')
            return ' '

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *sides):
        if len(sides) == self.sides_count:
            super().__init__(__color, list(sides))
        elif len(sides) == 1:
            super().__init__(__color, [sides[0]] * self.sides_count)
        else:
            super().__init__(__color,[1] * self.sides_count)

    def get_volume(self):
        side_cube = self.get_sides()[0]
        volume_cube = side_cube ** 3
        return volume_cube

# circle1 = Circle((200, 200, 100), 10)
# circle2 = Circle((200, 200, 100), 10, 15)
# print(circle1.get_color())
# circle1.set_color(55, 66, 77)
# print(circle1.get_color())
# print(circle1.get_sides())
# print(circle2.get_sides())
# circle1.set_sides(15)
# print(circle1.get_sides())
# print(len(circle1))
# print(len(circle2))
# print(circle1.get_radius())
# print(circle2.get_radius())
# print(circle1.get_square())
# print(circle2.get_square())

# triangle1 = Triangle((155,205,255,), 7,10,12)
# triangle2 = Triangle((155,205,255,), 7,10)
# print(triangle1.get_color())
# triangle1.set_color(305,120,400)
# print(triangle1.get_color())
# print(triangle1.get_sides())
# print(triangle2.get_sides())
# print(len(triangle1))
# print(len(triangle2))
# triangle1.set_sides(15,25,50)
# print(triangle1.get_sides())
# print(triangle1.get_square())

cube1 = Cube((222, 35, 130), 6)
print(cube1.get_sides())
cube2 = Cube((222, 35, 130), 6, 7)
print(cube2.get_sides())
print(cube1.get_volume())
print(cube2.get_volume())
print(len(cube1))
print(len(cube2))





