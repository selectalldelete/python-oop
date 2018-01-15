# Public -> member_name
# Protected -> _member_name
# Private -> __member_name

class Car:
    number_of_wheels = 4
    _color = 'Black'
    __year_of_manufacture = 2017 # _Car__year_of_manufacture

class Bmw(Car):
    def __init__(self):
        print('Protected attribute color:', self._color)

car = Car()
print('Public attribute number_of_wheels:', car.number_of_wheels)
bmw = Bmw()
print('Private attribute year_of_manufacture:', car._Car__year_of_manufacture)