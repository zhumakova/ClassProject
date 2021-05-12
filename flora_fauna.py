import inheritance


class Flora:

    def __init__(self, name, lifespan, habitat, plant_type):
        self.name = name
        self.lifespan = lifespan
        self.habitat = habitat
        self.plant_type = plant_type
        self.plant_size = 0


class Fauna:

    def __init__(self, name):
        self.name = name


class Predator(Fauna):

    def __init__(self, name:str, predator_type:str, what_eats:str, lifespan:int):
        super().__init__(name)
        self.predator_type = predator_type
        self.what_eats = what_eats
        self.lifespan = lifespan


    # def check_planet(self,planet:tsk4.Planet):
    #     if planet.fauna and not planet.humanity:
    #         print('YES')
    #     else:
    #         print('NO')


class Mammal(Fauna):

    def __init__(self, name, mammal_type, lifespan):
        super().__init__(name)
        self.mammal_type = mammal_type
        self.lifespan = lifespan


    def check_planet(self,planet:inheritance.Planet):
        if planet.flora and planet.fauna and not planet.humanity:
            planet.add_fauna(self)


shark = Predator('baby shark','sea','all',20)

giraffe = Mammal('malwan','earth',20)
giraffe.check_planet(inheritance.friendly)
marti = Mammal('marti','earth',20)
marti.check_planet(inheritance.friendly)
print(inheritance.friendly.__dict__)
print(inheritance.Planet.__dict__)


