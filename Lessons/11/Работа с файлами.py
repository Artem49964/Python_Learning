print('1.Открытие и закрытие файла')

file = open('file.txt', 'w') # Метод open позволяет нам открыть файл. Если файла нет то он создадится автоматически
#  вторым параметром мы указываем режим открытия. В нашем случае это формат для записи - 'w' - write
file.close() # Закрытие файла





print('2.Запись в файл')

file = open('file.txt', 'a')
file.write('Hello') # в наш файл было записано слово Hello
file.write('!') # Переноса и отступов в текстовом файле не последовало
file.write('\nMy name is Artem!') # запись в файл с переносом на новую строку
file.close()





print('3.Добаление данных в файл')

file = open('file.txt', 'a') # Открываем файл в режиме append (к текущей информации добавляется новая)
file.write('\nNew info from append mode')
file.close()





print('4.Режимы ввода')

file = open('file.txt', 'r') # read - режим для чтения (по умолчанию)
file.close()

file = open('file.txt', 'a') # append - добавляющий режим
file.close()

file = open('file.txt', 'w') # write - перезаписывющий режим
file.close()





print('5.Получение записи от пользователя и добавление данных в файл')

info = str(input('Ввдедите что нибудь: '))

file = open('file.txt', 'a')
file.write(info)
file.close()

new_info = str(123)
file = open('file.txt', 'a')
file.write('\n' + new_info)
file.close()





print('6.Считывание данных с файла')

file = open('file.txt', 'r')
print(file.read()) # Если мы не передаем никаких параметров то считается вся информация из файла

print(file.read(1)) # В случае передачи аргумента (int) будет получено колличество
# символов равно передаваемому аргументу


# Если же мы хотим считывать данные построчно, то нам нужно воспользоваться циклом:

file = open('file.txt', 'a')
file.write('\n' + '123' + '\n' + '456' + '\n' + '789' + '\n')
file.close()

file = open('file.txt', 'r')
for line in file:
    print(line) # мы увидим что у нас при выводе создалось 2 дополнительных перехода на новую строку.
#     Это произошло по той причине что итерации и также функция print добавляет по 1му переводу
#     на новую строку

# Для того что бы всё выводилось корректнонам нужно указать при выводе, что перехода на новую строку не будет:

for line in file:
    print(line, end='')

file.close()


























