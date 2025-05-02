import json
from docx import Document


def normalize_text(text: str) -> str:
    """
    Нормализует текст, убирая лишние пробелы и приводя к читаемому виду.
    """
    return '\n'.join(line.strip() for line in text.replace('\n', '\n').splitlines() if line.strip())


def extract_literature_block(doc_path: str) -> dict:
    """
    Извлекает текст от 'Список литературы' до
    'Политика академической честности и использование ИИ (AI)'.
    Разделяет на 'Обязательная литература', 'Дополнительная литература' и 'Интернет-ресурсы'.

    Args:
        doc_path (str): Путь к DOCX-файлу.

    Returns:
        dict: Словарь с разделенной литературой.
    """
    doc = Document(doc_path)
    result = {
        "Обязательная литература": [],
        "Дополнительная литература": [],
        "Интернет-ресурсы": []
    }
    current_section = None
    recording = False

    for para in doc.paragraphs:
        text = para.text.strip()

        # Пропускаем пустые строки, пока не начали запись
        if not recording:
            if text == "Список литературы":
                recording = True
            continue

        # Заканчиваем, если встретили конец блока
        if text.startswith("Политика академической честности"):
            break

        # Определяем текущий раздел
        if text in ["Обязательная литература", "Дополнительная литература", "Интернет-ресурсы"]:
            current_section = text
            continue

        # Если есть текущий раздел, добавляем текст в соответствующую категорию
        if current_section and text:
            result[current_section].append(normalize_text(text))

    # Форматируем результат
    for key in result:
        if result[key]:
            result[key] = '\n'.join(result[key])
        else:
            result[key] = "Данные отсутствуют"

    return result


if __name__ == "__main__":
    path = "media/Силлабус_Философия_2024-2025.docx"
    literature_data = extract_literature_block(path)
    json_data = json.dumps(literature_data, ensure_ascii=False, indent=4)
    print(json_data)
    with open("literature.json", "w", encoding="utf-8") as f:
        f.write(json_data)
