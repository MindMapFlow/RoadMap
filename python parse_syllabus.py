import logging
from typing import Dict, Any
from docx import Document

logger = logging.getLogger(__name__)


def parse_syllabus(file_path: str) -> Dict[str, Any]:
    """
    Парсит текст силлабуса из DOCX файла и возвращает структурированные данные,
    включая краткое описание курса, цель курса, ожидаемые результаты и методы обучения.
    """
    result = {
        "course_description": "",
        "course_objective": "",
        "learning_outcomes": "",
        "teaching_methods": ""
    }

    try:
        # Извлечение текста из DOCX
        doc = Document(file_path)
        lines = [para.text.strip() for para in doc.paragraphs if para.text.strip()]

        recording_description = False
        recording_objective = False
        recording_outcomes = False
        recording_methods = False
        description_lines = []
        objective_lines = []
        outcomes_lines = []
        methods_lines = []

        for line in lines:
            # Старт записи описания курса
            if "Краткое описание курса" in line:
                recording_description = True
                description_lines.append(line)
                continue

            # Переключение на цель курса
            if recording_description and line.startswith("Цель курса:"):
                recording_description = False
                recording_objective = True
                objective_lines.append(line)
                continue

            # Переключение на ожидаемые результаты
            if (recording_description or recording_objective) and line.startswith("Ожидаемые результаты:"):
                recording_description = False
                recording_objective = False
                recording_outcomes = True
                outcomes_lines.append(line)
                continue

            # Переключение на методы обучения
            if (recording_description or recording_objective or recording_outcomes) and line.startswith(
                    "Методы обучения:"):
                recording_description = False
                recording_objective = False
                recording_outcomes = False
                recording_methods = True
                methods_lines.append(line)
                continue

            # Остановка записи методов обучения при достижении следующей секции
            if recording_methods and line.startswith("Тематический план по неделям"):
                recording_methods = False
                break

            # Добавление строк в соответствующие списки
            if recording_description:
                description_lines.append(line)
            elif recording_objective:
                objective_lines.append(line)
            elif recording_outcomes:
                outcomes_lines.append(line)
            elif recording_methods:
                methods_lines.append(line)

        # Объединяем строки в единый текст
        result["course_description"] = "\n".join(description_lines)
        result["course_objective"] = "\n".join(objective_lines)
        result["learning_outcomes"] = "\n".join(outcomes_lines)
        result["teaching_methods"] = "\n".join(methods_lines)

        return result

    except Exception as e:
        logger.error(f"Ошибка парсинга DOCX: {str(e)}")
        raise


if __name__ == "__main__":
    path = "media/Силлабус_Философия_2024-2025.docx"
    try:
        syllabus_data = parse_syllabus(path)
        print(syllabus_data)
    except Exception as e:
        print(f"Ошибка: {str(e)}")