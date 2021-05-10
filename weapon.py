class Sword:

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
        self.__sword_type = None

    def sword_type(self,type):
        if type == 'rare':
            self.power *= 1.1
        elif type == 'legendary':
            self.power *= 1.7
        self.__sword_type = type
