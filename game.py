class Person:
    def __init__(self,name,race):
        self.name=name
        self.race=race
        self.power=5
        self.health=100
        self.defense=10
        self.stamina=10
        self.clothes=dict.fromkeys(['armor','weapon'])
        self.position=-1

    def set_armor(self,item):
        self.clothes['armor']=item
        self.power+=5
        self.health+=10
        self.defense+=5
        self.stamina-=4
    def set_weapon(self,item):
        self.clothes['weapon']=item



paladin=Person('Uther','human')
paladin.set_armor('plate')
paladin.set_weapon('sword')
print(paladin.__dict__)