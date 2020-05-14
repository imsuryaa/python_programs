#Polymorphism

class dog:
    def sound(self):
        print('Bow Bow..!')
class cat:
    def sound(self):
        print('Meow Meow..!')
def makesound(animal):
    animal.sound()

dogobj = dog()
catobj = cat()
makesound(dogobj)
makesound(catobj)