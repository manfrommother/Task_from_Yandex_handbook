class Rectangle():

    def __init__(self, a, b):
        self.a = a[0]
        self.b = a[1]
        self.c = b[0]
        self.d = b[1]

    def perimeter(self):
        total = self.a + self.b + self.c + self.d
        return int(total)


rect = Rectangle((1, 2), (3, 4))
print(rect.perimeter())