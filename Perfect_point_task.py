from math import sqrt

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def length(self, first_obj):
        return round(sqrt((self.x - first_obj.x) ** 2 + (self.y - first_obj.y) ** 2), 2)



second_point = Point(7, 9)
first_point = Point(2, -7)
print(second_point.length(first_point))