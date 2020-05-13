#Method Overriding

class A:
    def show(self):
        print('This is part of class A')

class B:
    def show(self):
        print('this part of class B')

b = B()
b.show()