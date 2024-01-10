class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self, name):
        super().__init__('Pug')
        self.name = name
    def make_sound(self):
        return "Woof Woof!"

my_dog = Dog("Danny")
print(f"{my_dog.name} is a {my_dog.species} and says {my_dog.make_sound()}")