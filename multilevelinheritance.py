class MusicalInstruments:
    number_of_major_keys = 12

class StringInstruments(MusicalInstruments):
    type_of_wood = 'Tonewood'

class Guitar(StringInstruments):
    def __init__(self):
        self.number_of_strings = 6
        print('Guitar has {} strings'.format(self.number_of_strings))
        print('It is made of {}'.format(self.type_of_wood))
        print('It can play {} major keys'.format(self.number_of_major_keys))

guitar = Guitar()