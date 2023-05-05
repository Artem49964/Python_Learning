# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Person created')
#
#     def sayHello(self):
#         print(f'\n{self.name} says hello!')
#
# class Student(Person):
#
#     def __init__(self, name, age, average_grade):
#         # Person.__init__(self, name, age)
#         super().__init__(name, age)
#         self.average_grade = average_grade
#
#     def study(self):
#         super().sayHello()
#         print(f'{self.name} studies, and his averge_grade = {self.average_grade}')
#
# class Teacher(Student):
#     pass
#
# person1 = Person('Tom', 19)
# student1 = Student('Ivan', 25, 4.2)
#
#
# student1.study()


#------------------------------------------------------------------------------------------------------------------------------------------------------



class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'\n{self.name} is eating')

bird = Animal('Kesha')
bird.eat()


class Dog(Animal):
    def __init__(self, breed, name):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f'\nDog with name {self.name} is barking')

dog = Dog('PitBull', 'Barbos')
dog.bark()


        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print(f'Cat with name {self.name} says Meow')

cat = Cat('Barsik')
cat.meow()



class Frog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f'Frog with {self.name} is eating')

frog = Frog('Qwaka')
frog.eat()



l = [1, 2, 3, 4, 5, 6, 7, 8]


c = [num * 2  for num in l]
print(c)


        



