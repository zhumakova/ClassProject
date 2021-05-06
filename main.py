# class Human:
#     def __init__(self,name,age,weight,height,gender):
#         self.name=name
#         self.age=age
#         self.weight=weight
#         self.height=height
#         self.gender=gender
#         self.soul=True
#         self.viruses=[]
#     def __str__(self):
#         return self.name+str(self.age)
# human1=Human(name='John',age=48,weight=90,height=185,gender='M')
# human2=Human(name='Sue',age=50,weight=40,height=160,gender='F')
# print(human1)

# class Human:
#     def __init__(self,name,age,weight,height,gender):
#         self.name=name
#         self.age=age
#         self.weight=weight
#         self.height=height
#         self.gender=gender
#         self.soul=True
#         self.viruses=[]
#     def __str__(self):
#         return self.name+str(self.age)
#     def __repr__(self):
#         return self.name
#     def add_viruse(self,viruse):
#         if viruse not in self.viruses:
#             self.viruses.append(viruse)
#
# human1=Human(name='John',age=48,weight=90,height=185,gender='M')
# human1.add_viruse('covid19')
# human1.add_viruse('flue')
# print(human1.viruses)

class Human:
    def __init__(self,name,age,weight,height,gender):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        self.gender=gender
        self.soul=True
        self.viruses=[]
        self.health=100
    def __str__(self):
        return self.name+str(self.age)
    def __repr__(self):
        return self.name
    def add_viruse(self,viruse):
        if viruse not in self.viruses:
            self.viruses.append(viruse)
            self.health-=10
            print(f'Человек болен {viruse}, текущее здоровье {self.health}')

human1=Human(name='John',age=48,weight=90,height=185,gender='M')
human2=Human(name='sue',age=48,weight=90,height=185,gender='M')
human3=Human(name='hue',age=48,weight=90,height=185,gender='M')

human1.add_viruse('covid')