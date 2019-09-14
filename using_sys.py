import sys
import os

if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')

print('Аргументы командной строки:')
for a in sys.argv:
    print(a)

print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

print(os.getcwd())
