
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'
print(shoplist)
print(shoplist.__len__())
shoplist.insert(0, 'вишня')
shoplist.__delitem__(1)
print(shoplist)
elem = 'бананы'
if elem in shoplist:
    shoplist.remove(elem)
    
print(shoplist)
# # Операция индексирования
# print('Элемент 0 -', shoplist[0])
# print('Элемент 1 -', shoplist[1])
# print('Элемент 2 -', shoplist[2])
# print('Элемент 3 -', shoplist[3])
# print('Элемент -1 -', shoplist[-1])
# print('Элемент -2 -', shoplist[-2])
# print(name)
# print('Символ 0 -', name[0])
# # Вырезка из списка
# print('Элементы с 1 по 3:', shoplist[1:3])
# print('Элементы с 2 до конца:', shoplist[2:])
# print('Элементы с 1 по -1:', shoplist[1:-1])
# print('Элементы от начала до конца:', shoplist[:])
# # Вырезка из строки
# print('Символы с 1 по 3:', name[1:3])
# print('Символы с 2 до конца:', name[2:])
# print('Символы с 1 до -1:', name[1:-1])
# print('Символы от начала до конца:', name[:])
