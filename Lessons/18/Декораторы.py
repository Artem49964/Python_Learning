class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def sound(self, sound):
        self.sound = sound

        print(f'This animal sounds like animal')


class Dog(Animal):
    def __init__(self, id, name, age, breed, food):
        self.breed = breed
        self.food = food
        self.id = id
        super().__init__(name, age)

    def barking(self):

        print(f'This dog with name {self.name} and breed {self.breed} is barking after eaten {self.food}')

dog1 = Dog(1, 'Barbos', 3, 'Dvor terier', 'korm')
dog1.barking()



