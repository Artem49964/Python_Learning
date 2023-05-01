print('1.Создание класса')

class Cat: # В родительском классе мы описываем глобальные характеристики для объекта:
    name = None
    age = None
    isHappy = None





print('2.Создание обїекта на основе класса')

# Теперь на основе класса мы можем создать объект:

cat1 = Cat()
cat1.name = 'Tom'
cat1.age = 3
cat1.isHappy = True


cat2 = Cat()
cat2.name = 'Барсик Мутант-Старожил'
cat2.age = 30
cat2.isHappy = False

print(cat1.name)
print(cat2.name)





print('3.Добавление методов в класс')

class Person:
    name = None
    age = None
    status = None
    region = None

    def set_data(self, name, age, status, region):# self это обязательный параметр, который позволит нам обращаться к полям класса (как this в JavaScript)
        self.name = name # Тут мы говорим что параметр функции set_data будет равен полю name родительского класса Person
        self.age = age
        self.status = status
        self.region = region

        # А теперь магия:

person1 = Person()
person1.set_data('Artem', 22, True, 'Ukraine')
print(person1.name, person1.age, person1.status, person1.region)


person2 = Person()
person2.set_data('Ivan', 30, False, 'USA')
print(person2.name, person2.age, person2.status, person2.region)



