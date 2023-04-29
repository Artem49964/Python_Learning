# Менеджер with as позволяет нам не закрывать файл после его открытия. В функции with as - close встроен. Например

print('1.Менеджер with as')

try:
    with open('../11/file.txt', 'a') as file:
        file.write('file was opened')
except TypeError:
    print('Ошибка типа')
else:
    print('Всё сработало отлично!')
