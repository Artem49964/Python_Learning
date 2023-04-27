print('1. Что такое множества')

# Множества это те же самые списки, но в множествах не может быть повторяющихся элементов

word = 'hello'
s = set(word)
print(s) # Как мы видим - символы расположены в случайном порядке без повторений

# Множества обычно используются для удаления повторяющихся элементов из списков






print('2.Создание множества')

s = {5, 7, 4, 2, 1, 9, 5} # Мы также используем фигурные скобки как и в словарях, но мы не указываем пару "key:value"
print(s)






print('3.Функции множеств')

s = {1, 2}
# Мы НЕ можем обращаться по индексу в множествах, так как значения расположены в случайном порядке
# Вместо этого мы можем удалять какие то значения и добавлять. Например:

s.add(3) # Добавляет один элемент в множество
print(s)

s.update([True, 'hello', 6, 7.2]) # Добавляет несколько элементов в множество
print(s)

s.remove('hello')
print(s)

s.pop() # Удаляет по умолчанию ПЕРВЫЙ элемент их множества
print(s) # В данном случае тут не с обратного, в отличии от списков






print('4.Удаление повторений из списка')

lisNums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(lisNums)

setNums = set(lisNums)
print(setNums)





print('5.Frozenset')

# Frozenset это тип данных set, но с функционалом котрежей. Мы не сможем их имзменять и весить они будут меняше

lis = [1, 1, 2, 3, 4, 4, 5, 'hello']
print(lis)

s = set(lis)
print(s)

frozen = frozenset(s)
print(frozen)










