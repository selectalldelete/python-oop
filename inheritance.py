# Write an object oriented program that performs the following tasks:
# 1. Create a class called Chair from the base class Furniture
# 2. Teakwood should be the type of furniture that is used by all furnitures by
# default
# 3. The user can be given an option to change the type of wood used for chair if
# he wishes to
# 4. The number of legs of a chair should be a property that should not be altered
# outside the class

class Furniture:
    def __init__(self):
        self._type_of_wood = 'Teakwood'

class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self.__number_of_legs = 4

    def set_wood_type(self):
        print('Enter new wood type:')
        self._type_of_wood = input()

    def print_chair_specs(self):
        print('Number of legs:', self.__number_of_legs)
        print('Type of wood:', self._type_of_wood)

chair = Chair()
while True:
    print('Enter 1 to view chair specs')
    print('Enter 2 to change wood type')
    print('Enter 3 to exit')
    user_input = int(input())
    if user_input == 1:
        chair.print_chair_specs()
    elif user_input == 2:
        chair.set_wood_type()
    elif user_input == 3:
        quit()