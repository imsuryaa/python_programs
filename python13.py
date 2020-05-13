#Multilevel inheritance

#base class
class employee:
    def name(self):
        print('Name of the employee')

#derived class 1
class department(employee):
    def depart(self):
        print('Department of the employee')

#derived class 2
class designation(department):
    def role(self):
        print('Designation of employee')

e1 = designation()
e1.name()
e1.depart()
e1.role()