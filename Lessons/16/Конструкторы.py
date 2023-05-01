print('3.Что такое конструкторы и как их использовать')

# За счёт конструктора мы можем выполнить определённый код при создании объекта. Возьмём код из пропрошлого занятия:

class Person:
    id = None
    name = None
    age = None
    status = None
    region = None

    def set_data(self, id, name, age, status, region):
        self.id = id
        self.name = name
        self.age = age
        self.status = status
        self.region = region

    def get_data(self):
        print('person_id -', self.id, 'person_name -', self.name, ', person_age -', self.age, ', person_status -', self.status, ', person_region -', self.region )

# Создадим конструктор внутри класса:

    def __init__(self, id, name, age, status, region):
        self.id = id
        self.name = name
        self.age = age
        self.status = status
        self.region = region
        self.get_data()

person1 = Person(0, 'Artem', 22, True, 'Ukraine')
person2 = Person(1, 'Ivan', 30, False, 'USA')

# Как мы можем увидеть - при испольовани конструктора мы используем меньше кода
