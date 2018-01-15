class Stone:
    stones = 0
    stone_collection = []
    def __init__(self, name):
        self.name = name
        Stone.stones += 1
        if Stone.stones <= 5:
            Stone.stone_collection.append(self.name)
        else:
            del Stone.stone_collection[0]
            Stone.stone_collection.append(self.name)

    @staticmethod
    def read_collection():
        print('Stones in collection:', Stone.stone_collection)

stone1 = Stone('Emerald')
stone2 = Stone('Ruby')
stone3 = Stone('Diamond')
stone4 = Stone('Amber')
stone5 = Stone('Sapphire')
stone5.read_collection()
stone6 = Stone('Onyx')
stone6.read_collection()