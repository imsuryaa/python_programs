# Inheritance
class car:                                      #base class
    def model(self):
        print('This is brand new Polo 2020')

class polo(car):                                #derived class
    def fuel(self):
        print("This car is petrol version")

print('Car details below')
c = polo()
c.model()
c.fuel()