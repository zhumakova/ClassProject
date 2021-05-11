class Armor:

    def __init__(self,name:str,size:int,weight:int,power:int,
                 desc='',stamina=0,health=0,defense=0):
        self.name = name
        self.desc = desc
        self.size = size
        self.weight = weight
        self.power = power
        self.stamina = stamina
        self.health = health
        self.defense = defense
        self.__armor_type = None

    def armor_type(self,type):
        if type == 'metal':
            self.power *= 2.1
        elif type == 'plastic':
            self.power *= 1.2
        self.__armor_type = type

    def __repr__(self):
        return self.name