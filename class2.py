class Employee:
    """
    описание сотрудников
    """
    def __init__(self,full_name:str,age:int,email:str,address:str,phone:str,position:str):
        self.full_name=full_name
        self.age=age
        self.email=email
        self.address=address
        self.phone=phone
        self.position=position
        self.salary=0

    def __repr__(self):
        return f'Сотрудник: {self.full_name}'
    def set_salary(self):
        if self.position=='developer':
            self.salary=100000
        elif self.position=='manager':
            self.salary=90000


john=Employee('john snow',18,'winter@gmail.com','winterfell','+123456','develop')
den=Employee('den',20,'den@gmail.com','moscow','+899998','manager')
den.set_salary()
print(den.salary)
den.__dict__['car']='Mercedes'
print(den.__dict__)
print(john)