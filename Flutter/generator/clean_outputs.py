import os
import re

def clean_markdown_files():
    # Регулярное выражение для поиска тегов <mytag>...</mytag>
    tag_pattern = re.compile(r'<think.*?</think>', re.DOTALL)
    
    # Обходим все файлы в текущей директории и подкаталогах
    for root, dirs, files in os.walk('..'):
        for file in files:
            file_path = os.path.join(root, file)
            if not (file.endswith('.md') or file.endswith('.markdown')):
                continue  # Пропускаем не-мardown файлы
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Удаляем содержимое между тегами
                cleaned_content = tag_pattern.sub('', content)
                
                # Разбиваем на строки для обработки
                lines = cleaned_content.split('\n')
                
                # Удалим пустые строки в начале и конце файла
                while lines and lines[0].strip() == '':
                    lines.pop(0)
                while lines and lines[-1].strip() == '':
                    lines.pop()
                
                # Сохраняем измененный контент обратно в файл
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
                
                print(f"✅ Обработан: {file_path}")
            except Exception as e:
                print(f"❌ Ошибка при обработке файла {file_path}: {e}")

if __name__ == '__main__':
    clean_markdown_files()
