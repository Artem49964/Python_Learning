print('1.Импортирование встроеных модулей')

# Модуль простыми словами это файл с функциями которые были написаны сторонними разработчиками.
# Обычно импорты пишутся в шапке файла с кодом
# Мы можем импортировать эти "файлы" и польоваться всеми функциями конкретного модуля. Например:


import time

time.sleep(1) # Функция sleep является асинхронной. То есть в нашем случае она заставляет дальнейший код
# подождать пока выполнится сама (По теме асинхронности в следующих конспектах). Параметром принимает int в качестве секунд

print(('Программа уже подождала 1 секунду...'))






print('2.Псевдонимы для модулей')

# К примеру мы импортировали какой то модуль, и его название довольно массивное. Мы можем задать переменную
# для этого модуля:

import dataclasses as dataClass

print(dataClass.is_dataclass(1)) # Теперь мы можем обращаться к модулям по указаным для них перемеенным





print('Создание и импортирование собственного модуля')

# Мы можем импортировать отдельные функции из конкретного модуля. Например:

from mymodule import sayHello

sayHello()





print('3.Пакетный менеджер pip')

# Для установки невтроеных модулей используется пакетный менеджер pip

# В терминале нужно прописать команду pip install название модуля. Точную команду нажно смотреть в документации
# к конкретному модулю

