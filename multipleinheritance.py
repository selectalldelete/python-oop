# Three classes - two base, one derived

class OperatingSystem: # Base
    multitasking = True
    name = 'Mac OS'

class Apple: # Base
    website = 'www.apple.com'
    name = 'Apple'

class MacBook(OperatingSystem, Apple): # Derived
    def __init__(self):
        if self.multitasking:
            print('This is a multitasking system')
            print('Visit {} for more details'.format(self.website))
            print('Name:', self.name) # if conflict, inheritance order matters

macbook = MacBook()