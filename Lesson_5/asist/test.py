<<<<<<< HEAD
import os

# Указываем путь к папке (можно '.' — это текущая папка)
path = 'C:\\Users\\tanku\\OneDrive\\Desktop\\asist'
  # или, например, 'C:/Users/твой_путь/'

# Получаем список файлов и папок
contents = os.listdir(path)

# Выводим содержимое
print(f"Содержимое папки {os.path.abspath(path)}:")
for item in contents:
    print(item)
=======
import os

# Указываем путь к папке (можно '.' — это текущая папка)
path = 'C:\\Users\\tanku\\OneDrive\\Desktop\\asist'
  # или, например, 'C:/Users/твой_путь/'

# Получаем список файлов и папок
contents = os.listdir(path)

# Выводим содержимое
print(f"Содержимое папки {os.path.abspath(path)}:")
for item in contents:
    print(item)
>>>>>>> 2966b74bb9f1d541460a6175f52c9ffb3311c9b7
