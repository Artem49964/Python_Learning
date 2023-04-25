print('1.Условный оператор if. Матемачические проверки')
if 5==5:
    print('Отличная работа! 5 равно 5')

if 4!=5:
    print('Отличная работа! 4 не равно 5')


user_data = int(input('Введите число: '))

if user_data > 5:
    print('Вы ввели число которое больше чем 5')

print('2.Оператор else. Булевые проверки')
isHappy = True

if not isHappy: # дериктива "not" означает проверку на значение True - False
    print('Пользователь не счастлив!( Давайте веселить его!')
else:
    print("Все в порядке!")

print('3.Оператор elif')
isHappy = True # В зависимости от значения мы будем получать тот или иной результат

if isHappy: # Проверка на то, является ли переменная True
    print('Все в порядке!')

elif not isHappy: # Проверка на то, является ли переменная False
    print("Пользователь не счастлив!( Давайте веселить его!")

else:
    print('Что то пошло не так!')

print('4.Несколько условий')
isHappy = False
user_data = int(input('Введите число 5: '))

if isHappy and user_data == 5:
    print('isHappy==True и Вы ввели число 5!')
elif not isHappy or user_data!=5:
    print('isHappy!=True или Вы не ввели число 5!')

print('5.Тернарный оператор')
s = str(input("Введите значение Five: "))
num = 5 if s=="Five" else 0 # Тут мы говорим что num будет равно 5 только в том случае если s равна Five. Иначе num будет равна 0
print("num =", num)





