
import pickle


# список покупок
shop_list = ['яблоки', 'манго', 'морковь']
# Запись в файл
f = open('shop_list.data', 'wb')
pickle.dump(shop_list, f)  # помещаем объект в файл
f.close()
del shop_list  # уничтожаем переменную shoplist
# Считываем из хранилища
f = open('shop_list.data', 'rb')
stored_list = pickle.load(f)  # загружаем объект из файла
print(stored_list)
