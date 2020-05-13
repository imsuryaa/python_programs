#Mutliple inhheritance

#base class 1
class father:
    def f_name(self):
        print('Alex Costra is my father')

#base class 2
class mother:
    def m_name(self):
        print('Rox Milly is my mother')

#derived class
class child(father,mother):
    def c_name(self):
        print('My name is Paul Andrew')

family = child()
family.c_name()
family.f_name()
family.m_name()