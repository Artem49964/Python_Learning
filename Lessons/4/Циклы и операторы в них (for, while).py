print("1.Цикл for")
# for i in range(10): # метод range принимает 3 параметра. 1й параметр - диапазон итерации
#     print(i) # Выведутся число от 0 до 10 не включительно
#
# for i in range(10, 20): # 2й параметр - стартовая позиция, с какой точки начинать отчёт(a - start, b - end(не включительно))
#     print(i) # Выведутся число от 10 до 20 не включительно
#
# for i in range(20, 30, 2): # 3й параметр - с каким шагом нужно выполнять код
#     print(i)  # Выведутся число от 20 до 29 не включительно с шагом 2
#
#
# word = str(input('Введите что нибудь: '))
# # for i in word:
# #     print(i) # Выведутся поочерёрдно все символы переменной word
#
#
# count = 0
# for i in word:
#     if i!=word:
#         count += 1
#         print(count)
#     else:
#         print("Error")

print("2.Цикл while")
# i = 0
# while i != 10: пока условие True - программа будет выполняться
#     i += 1
#     print(i)

print("3.Операторы циклов. break, continue")
# for i in range(1, 11):
#     if i>5:
#         break # Оператор break останавливает выполнение программы как только условие True
#     print(i)

# for i in range(1, 11):
#     if i % 2 == 0: # Если при делении на 2 будет остача 0: то
#         continue # Оператор continue пропускает одну итерацию как только условие True и программа продолжает выполняться
#     print(i)

print('4.Поиск символа в строке')
# found = None
# word = 'hello'
#
# for i in word:
#     if i == 'l':
#         found = True
#         break
#     else:
#         found = False
# print(found)
