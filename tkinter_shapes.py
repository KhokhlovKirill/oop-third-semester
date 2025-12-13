from tkinter import *


class Shape:
    def __init__(self):
        pass


class Point(Shape):
    def __init__(self, x, y):
        super().__init__()
        self.__coordinates = (x, y)

    @property
    def x(self):
        return self.__coordinates[0]

    @property
    def y(self):
        return self.__coordinates[1]

    def draw(self, canvas):
        canvas.create_oval(self.x - 3, self.y - 3, self.x + 3, self.y + 3, fill='black')


class Line(Shape):
    def __init__(self, a: Point, b: Point):
        super().__init__()
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def draw(self, canvas):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y)


class Triangle(Shape):
    def __init__(self, a: Point, b: Point, c: Point):
        super().__init__()
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

    def draw(self, canvas):
        sides = (Line(self.a, self.b),
                 Line(self.b, self.c),
                 Line(self.c, self.a))
        for s in sides:
            s.draw(canvas)


class Rectangle(Shape):
    def __init__(self, bottom_left: Point, top_right: Point):
        super().__init__()
        self.__bottom_left = bottom_left
        self.__top_right = top_right

    @property
    def bottom_left(self):
        return self.__bottom_left

    @property
    def top_left(self):
        return Point(self.bottom_left.x, self.top_right.y)

    @property
    def top_right(self):
        return self.__top_right

    @property
    def bottom_right(self):
        return Point(self.top_right.x, self.bottom_left.y)

    def draw(self, canvas):
        sides = (Line(self.bottom_left, self.top_left),
                 Line(self.top_left, self.top_right),
                 Line(self.top_right, self.bottom_right),
                 Line(self.bottom_right, self.bottom_left))
        for s in sides:
            s.draw(canvas)


class Circle(Shape):
    def __init__(self, center: Point, radius):
        super().__init__()
        self.__center = center
        self.__radius = radius

    @property
    def center(self):
        return self.__center

    @property
    def radius(self):
        return self.__radius

    def draw(self, canvas):
        canvas.create_oval(self.center.x - self.radius, self.center.y - self.radius, self.center.x + self.radius,
                           self.center.y + self.radius)


root = Tk()
root.title('')
root.geometry('800x700')

canvas = Canvas(bg='#FFFFFF', width=800, height=700)
canvas.pack()

p1 = Point(100, 100)
p2 = Point(300, 100)
p3 = Point(200, 500)
p4 = Point(500, 600)
t = Triangle(p1, p2, p3)
c = Circle(p3, 50)
t.draw(canvas)
c.draw(canvas)
l = Line(p2, p4)
l.draw(canvas)

p1.draw(canvas)
p2.draw(canvas)
r = Rectangle(p1, p4)
r.draw(canvas)

root.mainloop()
