
class Planet:

    def __init__(self, name, size, loc):
        self.name = name
        self.size = size
        self.loc = loc
        self.population = 0
        self.temp = 0
        self.sats = []
        self.humanity = False
        self.water = False
        self.oxygen = False
        self.flora = False
        self.fauna = False
        self.flora_list = None
        self.fauna_list = None


    def add_sat(self, sat_list: list):
        for sat in sat_list:
            if sat not in self.sats:
                self.sats.append(sat)

    def set_humanity(self):
        if self.temp >= -20 and self.water and self.oxygen:
            self.humanity = True
        else:
            self.humanity = False

    def set_flora_and_fauna(self):
        flag = None
        if self.water and self.oxygen and self.temp >= -50:
            flag = True
        else:
            flag = False
        self.fauna = flag
        self.flora = flag

    def set_live(self):
        flag = None
        if self.flora and self.fauna:
            self.flora_list = []
            self.fauna_list = []

    def add_fauna(self,animal):
        if self.fauna_list is not None:
            if animal not in self.fauna_list:
                self.fauna_list.append(animal)




"""MRO"""


class Giant(Planet):
    def __init__(self,name,size,loc):
        super().__init__(name,size,loc)
        self.size += 100


class Soil(Giant):
    pass

class Gas(Giant):

    def __init__(self, name, size, loc, gas_type):
        super().__init__(name, size, loc)
        self.gas_type = gas_type
        self.temp = -273

    def set_humanity(self):
        if self.temp >= -20 and self.gas_type == 'O':
            self.humanity = True
            print(f'Планета: {self.name} пригодна для жилья!')
        else:
            print(f'Планета: {self.name} не пригодна для жилья!')
            self.humanity = False

    def add_population(self, people_count):
        if self.humanity:
            self.population += people_count







friendly = Gas('Friend', 30, 'andromeda', 'O')
friendly.temp = -19

friendly.add_population(100)

friendly.water = True
friendly.oxygen = True

friendly.set_flora_and_fauna()
friendly.set_live()


"""
1. Создать класс Soil,Giants
"""