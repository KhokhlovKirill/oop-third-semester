import math

class Shape:
    def __init__(self):
        pass

    @property
    def perimeter(self):
        raise NotImplementedError

    @property
    def area(self):
        raise NotImplementedError

    @property
    def diameter(self):
        raise NotImplementedError

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()

        if (a <= 0) or (b <= 0) or (c <= 0):
            raise TypeError('The side must be positive')

        if not ((a + b > c) and (a + c > b) and (b + c > a)):
            raise TypeError('This rectangle does not exist')

        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

    @property
    def diameter(self):
        return max(self.a, self.b, self.c)

    def __str__(self):
        return f'Triangle: {self.a}, {self.b}, {self.c}'

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()

        if (a <= 0) or (b <= 0):
            raise TypeError('The side must be positive')

        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    @property
    def area(self):
        return self.a * self.b

    @property
    def diameter(self):
        return (self.a**2 + self.b**2)**0.5

    def __str__(self):
        return f'Rectangle: {self.a}, {self.b}'

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return f'Square: {self.a}, {self.b}'

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()

        if radius <= 0:
            raise TypeError('The radius must be positive')

        self.__r = radius

    @property
    def r(self):
        return self.__r

    @property
    def diameter(self):
        return self.r * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.r

    @property
    def area(self):
        return math.pi * self.r**2

    def __str__(self):
        return f'Circle: radius {self.r}'
