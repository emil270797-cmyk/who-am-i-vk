import os

# Сюда мы будем собирать все слова
databases = {}

# Читаем файл movies.txt
if os.path.exists('movies.txt'):
    with open('movies.txt', 'r', encoding='utf-8') as file:
        # Читаем строки, убираем пробелы, оставляем только непустые
        words = [line.strip() for line in file if line.strip()]
        databases['movies'] = words
        print(f"? Успешно прочитано {len(words)} слов из movies.txt")
else:
    print("? Файл movies.txt не найден!")

# Создаем файл words.js, который поймет браузер
with open('words.js', 'w', encoding='utf-8') as js_file:
    # Записываем словарь в виде JavaScript переменной
    js_file.write(f"const databases = {databases};\n")
    print("? Файл words.js успешно создан!")