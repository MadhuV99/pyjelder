# Classes

class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

    def profile(self):
        print("Side Length:", self.side)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

my_square = Square(5)
my_square.profile()

