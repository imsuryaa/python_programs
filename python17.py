# Encapsulation, accesing private variable

class car:
    __topspeed = 0
    __name = " "
    def __init__(self):
        self.__topspeed = 160
        self.__name = "Honda City"
    def version(self):
        print('petrol version')
        print(self.__name)
        print(self.__topspeed)
    def setname(self,name):
        self.__name = name
        print(self.__name)

model = car()
model.version()
model.setname('Honda Jazz')