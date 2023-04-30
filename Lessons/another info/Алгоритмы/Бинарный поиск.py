# Логика бинарного поиска заключается в том что бы уменьшить колличество попыток поииска посредством
# исключением половины имеющихся в ТЕКУЩИЙ момент чисел. Например:

# Бинарный поиск работает только тогда когда массив отсортирован


lis = [9, 6, 3, 7, 5, 3, 6, 8, 3, 6]
lis.sort()

print(lis) # [3, 3, 3, 5, 6, 6, 6, 7, 8, 9]

# low = 0
# high = len(lis) - 1
# mid = int((low + high) / 2)
# guess = lis[mid]
# # if guess < item:
# #     mid + 1

def binary_search(lis, item): # В переменных low и high хранятся границы той части списка где выполняется поиск
    low = 0
    high = len(lis) - 1

    while low <= high: # Пока эта часть не сократится до одного элемента проверяем следующий элемент
        mid = (low + high)
        guess = lis[mid]

        if guess == item: # значение найдено
            return mid
        elif guess > item: # Много
            high = mid - 1
        else: # Мало
            low = mid + 1 # Значение не существует
        return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # => 1 # Вспомним что нумерация элементов начинается с 0. Значит второй ячейке соотвествует индекс 1
print(binary_search(my_list, -1)) # => Элемент не найден


# Задача

# Есть список на 128 имен. Написать функцию которая определяет колличество попыток на поиск нужного:

names_list = []

def search_name(lis, item):
    # Для начала наполним список:

    for i in range(128):
        names_list.append(i + 1)
    print(names_list)

    low = 0
    high = len(lis)
    mid = (low + high) / 2

    while mid < item:
        pass









