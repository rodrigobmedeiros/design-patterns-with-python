class Singleton(object):

    _instance = None

    def __new__(self, *args, **kwargs):

        if self._instance is None:

            self._instance = super(Singleton, self).__new__(self)

        return self._instance

# Learn more abour super() method
class Rectangle():

    def __init__(self, length, width):

        print('__init__ from Rectangle')
        self.length = length 
        self.width = width

    def area(self):

        return self.length * self.width 
    
    def perimeter(self):

        return 2 * self.length +\
            2  * self.width 

class Square(Rectangle):

    def __init__(self, length):

        print('__init__ from Square')
        super().__init__(length, length)

class Cube(Square):

    def __init__(self, length):

        print('__init__ from Cube')
        super(Square, self).__init__(length, length)
        self.face_area = super().area()

    def surface_area(self):

        return self.face_area * 6

    def volume(self):

        return self.face_area * self.width

rectangle = Rectangle(1, 2)
print(f'area = {rectangle.area()}')
print(f'perimeter = {rectangle.perimeter()}')

square = Square(2)
print(f'area = {square.area()}')
print(f'perimeter = {square.perimeter()}')

cube = Cube(2)
print(f'surface area = {cube.surface_area()}')
print(f'volume = {cube.volume()}')

sing_1 = Singleton()
sing_2 = Singleton()

print(f"object 1: {sing_1}")
print(f"object 2: {sing_2}")