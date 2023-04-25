print('1.Cтрока это список') # Данное утрверждение не является ложным.
# Речь идёт не как о типе данных, а как о некоторых функциях, которые применимы как к спискам так и к строкам
# Давайте в этом убедимся:

word = 'Name'
print(len(word)) # 4

print(word.count('N')) # 1

# Строка это по сути список со значениями, но своебразный
# Поэтому у строк есть отдельные функции. Ниже их рассмотрим:

print(word.upper()) # Приводит строку к верхнему регистру
print(word.lower()) # Приводит строку к нижнему регистру

print(word.isupper()) # Возвращает нам True иил False в зависимости от того в каком регистре находится строка.
print(word.islower())

print(word.capitalize()) # Приводит первую букву строки к верхненму регистру, а все остальные буквы к нижнему

print(word.find('m')) # Метод find ищет передаваемое в параметры значение, и возвращает индекс того символа которого нашел

word = 'Name SurName LastName' # Предположим что у нас есть строка с n-колличеством значений. Сделаем список методом split()
print(word.split()) # метод split возвращает список. Параметром указываем значение, которым будем розделять элементы списка
# По умолчанию это будет split






# Задача - у нас есть строка letters. нам нужно его проитерировать и привести каждый элемент к верхнему регистру:

letters = 'a, b, c'

# Методом split() сделаем из нашей строки список:
lis = letters.split(', ')

# Создадим циикл и укажем для него диапазон равен длинне нашего списка строки:
for i in range(len(lis)):

    # Далее мы каждому элементу(по инлдексу) нашего списка будем присваивать его же элемент, но
    # приведэный к верхнему регистру методом upper
    lis[i] = lis[i].upper()

    print(lis[i]) # И выведем результат. Это будет результат всех итераций - элементы списка приведённых к верхнему регистру

result = ', '.join(lis) # Методом join приведём наш список обратно к строке
print(result)








