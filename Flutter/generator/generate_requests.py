# pip3 install lmstudio

import os
import json
import lmstudio as lms

# Константы для шаблонов prompt
PROMPT_INTRODUCTION = """Представь, что ты личный тренер по программированию. 
Дай подробную лекцию. Если требуются примеры, давай их для языка dart и flutter. 
Лекция должна быть самодостаточна для самоподготовки мобильного flutter разработчика уровня """

PROMPT_TOPIC = "Тема лекции:\n"

PROMPT_QUESTIONS = "Список вопросов:\n"

PROMPT_ADDITIONAL_CONTENT = """
В конце помести:
1. практическое задание 
2. контрольные вопросы по теме.
3. список литературы и ссылок для дополнительного чтения.

Текста надо побольше и описывать все максимально подробно. Лекция должна быть самодостаточной и исчерпывающей. Каждая тема должна сопровождаться подробным текстовым описанием и исчерпывающими примерами с комментариями
"""

def load_topics_from_json(file_path: str) -> list:
    """Загрузить данные из JSON-файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Ошибка загрузки данных из файла {file_path}: {e}")

def create_directories(base_dir: str) -> None:
    """Создать необходимые директории"""
    os.makedirs(base_dir, exist_ok=True)

def generate_content_for_file(topic_info: dict, model) -> str:
    """
    Сгенерировать содержимое файла для заданной темы
    :param topic_info: Словарь с информацией о теме (level, topic, details)
    :return: Сгенерированный текст
    """
    level = topic_info['level']
    topic = topic_info['topic']
    details = topic_info['details']
    
    # Формирование prompt для генерации лекции
    subtopics_list = "- " + "\n- ".join(details) + "\n"
    full_prompt = (
        PROMPT_INTRODUCTION 
        + level 
        + PROMPT_TOPIC 
        + topic 
        + PROMPT_QUESTIONS 
        + subtopics_list 
        + PROMPT_ADDITIONAL_CONTENT
    )

    return model.respond(full_prompt).content

def create_tutorials_structure():
    """Создать структуру tutorials на основе данных из JSON-файла"""
    # Путь к JSON-файлу с топиками
    topics_file = 'topics/all_topics.json'
    
    try:
        # Загрузка данных из файла
        topics_data = load_topics_from_json(topics_file)
        
        # Основная директория для tutorials
        tutorials_dir = 'tutorials'
        create_directories(tutorials_dir)
        
        # Обработка каждого элемента из JSON-файла
        for item in topics_data:
            level = item['level']
            topic = item['topic']
            
            # Формирование имени файла (замена слешей на подчёркивания)
            file_name = topic.replace('/', '_') + ".md"
            
            # Создание директории уровня
            level_path = os.path.join(tutorials_dir, level)
            create_directories(level_path)
            
            # Полный путь к файлу
            file_path = os.path.join(level_path, file_name)
            
            # Генерация и запись содержимого файла
            with open(file_path, 'w', encoding='utf-8') as f:
                content = generate_content_for_file(item, model)
                f.write(content)

        print("Структура tutorials успешно создана!")

    except Exception as e:
        print(f"Ошибка при обработке: {e}")

if __name__ == "__main__":
    # Инициализация модели
    model = lms.llm("qwen3-14b")
    
    # Создание структуры tutorials
    create_tutorials_structure()
