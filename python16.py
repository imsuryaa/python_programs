# Encapusulation

class car:
    def __init__(self):
        self.__updatesoft()                     #private method
    def driving(self):
        print('Driving')
    def __updatesoft(self):
        print('updating drivers in console')

ride = car()
ride.driving()