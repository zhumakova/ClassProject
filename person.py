import weapon
import armor


class Person:

    def __init__(self,name,race):
        self.name = name
        self.race = race
        self.power = 5
        self.health = 100
        self.defense = 10
        self.stamina = 10
        self.clothes = dict.fromkeys(['armor','weapon'])
        self.position = -1

    def set_armor(self,item):
        self.clothes['armor'] = item
        self.power += 3
        self.health += 10
        self.defense += 5
        self.stamina -= 4

    def set_weapon(self,item:weapon.Sword):
        self.clothes['weapon'] = item
        self.power += item.power
        self.health += item.health
        self.stamina += item.stamina
        self.defense += item.defense


