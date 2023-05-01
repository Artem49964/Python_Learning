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
    id = None
    name = None
    age = None
    status = None
    region = None

    def set_data(self, id, name, age, status, region):# self это обязательный параметр, который позволит нам обращаться к полям класса (как this в JavaScript)
        self.id = id # Тут мы говорим что параметр функции set_data будет равен полю id родительского класса Person
        self.name = name
        self.age = age
        self.status = status
        self.region = region

    def get_data(self):
        print('person_id -', self.id, 'person_name -', self.name, ', person_age -', self.age, ', person_status -', self.status, ', person_region -', self.region )

        # А теперь магия:

person1 = Person()
person1.set_data(0, 'Artem', 22, True, 'Ukraine') # То есть теперь мы можем сделать код более "сухим", воспользовавшись функцией
person1.get_data()


person2 = Person()
person2.set_data(1, 'Ivan', 30, False, 'USA')
person2.get_data()



