

class ShortInputException(Exception):
    ''' Пользовательский класс исключения. '''
    def __init__(self, length, at_least):
        Exception.__init__(self)
        self.length = length
        self.at_least = at_least


try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
# Здесь может происходить обычная работа
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введённой строки -- {0}; \
ожидалось, как минимум, {1}'.format(ex.length, ex.at_least))
else:
    print('Не было исключений.')
