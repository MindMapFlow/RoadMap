import re
import logging
from typing import Dict, Any, Optional
from docx import Document

logger = logging.getLogger(__name__)

def parse_syllabus(content: str) -> Dict[str, Any]:
    """
    Парсит текст силлабуса и возвращает структурированные данные.
    Обрабатывает форматы с неделями, темами, подтемами и материалами.
    """
    result = {
        "topics": [],
        "dependencies": [],
        "materials": []
    }

    current_week = None
    current_topic = None
    week_counter = 0
    topic_counter = 0

    lines = [line.strip() for line in content.split('\n') if line.strip()]

    for line in lines:
        # Обработка недель
        week_match = re.match(r'^(Неделя|Week)\s*(\d+)[.:]?\s*(.*)', line, re.IGNORECASE)
        if week_match:
            week_counter += 1
            week_title = f"{week_match.group(1)} {week_match.group(2)}"
            if week_match.group(3):
                week_title += f": {week_match.group(3)}"

            current_week = {
                "title": week_title,
                "description": "",
                "order": week_counter,
                "subtopics": []
            }
            result["topics"].append(current_week)
            current_topic = None
            topic_counter = 0
            continue

        # Обработка тем
        topic_match = re.match(r'^(Тема|Topic)\s*(\d+)[.:]\s*(.+)', line, re.IGNORECASE)
        if topic_match and current_week:
            topic_counter += 1
            current_topic = {
                "title": topic_match.group(3).strip(),
                "description": "",
                "order": topic_counter,
                "subtopics": []
            }
            current_week["subtopics"].append(current_topic)
            continue

        # Обработка подтем (маркированные списки)
        subtopic_match = re.match(r'^[-•*]\s*(.+)', line)
        if subtopic_match and current_topic:
            current_topic["subtopics"].append({
                "title": subtopic_match.group(1).strip(),
                "description": "",
                "order": len(current_topic["subtopics"]) + 1
            })
            continue

        # Обработка материалов
        material_match = re.match(
            r'^(Материалы|Materials|Литература|Literature|Задания|Assignments|Ресурсы|Resources):?\s*(.+)',
            line,
            re.IGNORECASE
        )
        if material_match and (current_topic or current_week):
            target = current_topic if current_topic else current_week
            result["materials"].append({
                "topic": target["title"],
                "type": "article",  # Будет уточнено GPT
                "title": material_match.group(1).strip(),
                "content": material_match.group(2).strip(),
                "url": ""
            })

    # Создаем зависимости между неделями
    for i in range(1, len(result["topics"])):
        result["dependencies"].append({
            "from": result["topics"][i-1]["title"],
            "to": result["topics"][i]["title"]
        })

    return result

def extract_text_from_docx(file_path: str) -> str:
    """Извлекает текст из DOCX файла с сохранением структуры"""
    try:
        doc = Document(file_path)
        return "\n".join(para.text for para in doc.paragraphs if para.text.strip())
    except Exception as e:
        logger.error(f"Ошибка чтения DOCX: {str(e)}")
        raise