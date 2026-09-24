import os
import glob
import json

databases = {}

# Автоматически находим ВСЕ текстовые файлы в папке
for filepath in glob.glob("*.txt"):
    category_name = os.path.splitext(filepath)[0] # Имя файла станет ID категории
    with open(filepath, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
        databases[category_name] = words
        print(f"✅ Добавлено {len(words)} слов из {filepath}")

# Сохраняем в JS-файл
with open('words.js', 'w', encoding='utf-8') as js_file:
    # json.dumps аккуратно обработает все кавычки и запятые
    js_data = json.dumps(databases, ensure_ascii=False)
    js_file.write(f"const databases = {js_data};\n")
    print("🚀 Файл words.js успешно собран из всех словарей!")
