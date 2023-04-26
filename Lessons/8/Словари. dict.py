print('1.Словари. Создание и наполнение')

# Для создания словаря нам нужно использовать фигурные скобки
diction = {}

# Данные в словарях хранятся по принипу "ключ:значение". Например:
diction = {"name":'Artem'}
print(diction['name']) # обращение к значениям словаря осуществляются по ключу [].


# Мы можем хранить несколько значенией в качестве кортежа в одном ключе. Например:
diction = {'user_1':('Name', 'LastName', 'SurName')}
print(diction)


# И наоборот - кортеж для одного значения. Например:
diction = {('Name', 'LastName', 'SurName'):'user_2'}
print(diction)





print('2.Альтернативные записи словаря')

user = dict(name_age=('userName', 100), surname='userSurname')
print(user)
print(user['name_age'])





print('3.Вывод словаря через цикл')

# Если мы попробуем роитерировать словарь то получим его значения. Давайте в этом убедимся:

diction = {"name":'Artem', 'surname':'userSurname'}

for i in diction:
    print(i) # name
             # surname

# Как мы видим выводятся только ключи. Что бы выводить значения нам нужно использовать функцию items, а также добавить
#  еще один итератор в цикл

print(diction.items()) # ([('name', 'Artem'), ('surname', 'userSurname')])

for key, value in diction.items():
    print(key + ' - ' + value)





print('4.Функции для работы с словарями')

diction = {"name":'Artem', 'surname':'userSurname'}

dic = diction.get('name') # Методом get мы можем помещать значение ключа в переменную
print(dic)

# print(diction.pop('name')) # Удаляет пару по ключу и возвращает значение

# (diction.popitem()) # Удаляет последнюю пару из словаря
print(diction)

print(diction.keys()) # Возвращает все ключи словаря

print(diction.values()) # Возвращает все значения словаря

print(diction.items()) # dict_items([('name', 'Artem'), ('surname', 'userSurname')])

diction['name'] = 'Dmytro' # Изменение значения ключа
print(diction)





print('4.Описание человека')

person = {
    "user_1":{
        "name":'Sergey',
        "surname":'Sergeev',
        "age": 11,
        "status":True
    },

    "user_2":{
        "name":'Ivan',
        "surname":'Ivanov',
        "age": 22,
        "status":False
    },

    "user_3":{
        "name":'Boris',
        "surname":'Borisov',
        "age": 33,
        "status":None
    }
}










