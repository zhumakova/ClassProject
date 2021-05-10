"""
Создать класс Armor со всеми характеристиками персонажа для брони: health,power,defense,stamina
1. Создать метод armor_type по примеру в Sword
2. Сгенерировать обьекты мечей и брони
"""
import person
import weapon
import armor

person_info_dict = {
    'name':['john','vova','aliya','begimai','erbol'],
    'race':['orc','human','human','elf','human']
}

person_database = []
for index,names in enumerate(person_info_dict['name']):
    new_person = person.Person(name=names, race=person_info_dict['race'][index])
    person_database.append(new_person)
# print(person_database[0].__dict__)

import random
import string
letters=string.ascii_letters
armor_info_dict = {
    'name':['army','pretty','crash','sexy','hot'],
    'desc':[''.join(random.choice(letters) for i in range(5))],
    'size':[random.randint(1,10) for i in range(5)],
    'weight':[random.randint(1,20) for i in range(5)],
    'power':[random.randint(1,100) for i in range(5)],
    'stamina':[random.randint(1,25) for i in range(5)],
    'health':[random.randint(1,55) for i in range(5)],
    'defense':[random.randint(1,55) for i in range(5)]
}
print(armor_info_dict['desc'])
armor_database = []
for index,names in enumerate(armor_info_dict['name']):
    new_armor = armor.Armor(name=names,desc=armor_info_dict['desc'][0][index],
                            size=armor_info_dict['size'][index],
                            weight=armor_info_dict['weight'][index],
                            power=armor_info_dict['power'][index],
                            stamina=armor_info_dict['stamina'][index],
                            health=armor_info_dict['health'][index],
                            defense=armor_info_dict['health'][index])


    armor_database.append(new_armor)

# print(armor_database[0].__dict__)


import random
import string
letters=string.ascii_letters
sword_info_dict = {
    'name':['nice','cute','lazy','curve','straight'],
    'desc':[''.join(random.choice(letters) for i in range(5))],
    'size':[random.randint(1,10) for i in range(5)],
    'weight':[random.randint(1,20) for i in range(5)],
    'power':[random.randint(1,100) for i in range(5)],
    'stamina':[random.randint(1,25) for i in range(5)],
    'health':[random.randint(1,55) for i in range(5)],
    'defense':[random.randint(1,55) for i in range(5)]
}
print(sword_info_dict['desc'])

sword_database = []
for index,names in enumerate(sword_info_dict['name']):
    new_sword =weapon.Sword(name=names,desc=sword_info_dict['desc'][0][index],
                            size=sword_info_dict['size'][index],
                            weight=sword_info_dict['weight'][index],
                            power=sword_info_dict['power'][index],
                            stamina=sword_info_dict['stamina'][index],
                            health=sword_info_dict['health'][index],
                            defense=sword_info_dict['health'][index])
    sword_database.append(new_sword)





for key,value in person_database[0].__dict__.items():
    if isinstance(value,dict):
        value['armor']=armor_database[0].__dict__['name']
        value['weapon']=sword_database[0].__dict__['name']
# person1=weapon.Sword.sword_type('rare')

print(sword_database[0].__dict__)
print(armor_database[0].__dict__)

person_database[0].set_armor(armor_database[0])
person_database[0].set_weapon(sword_database[0])
print(person_database[0].__dict__)


