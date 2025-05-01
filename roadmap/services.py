import openai
import json
import logging
from django.conf import settings
from typing import Dict, Any

logger = logging.getLogger(__name__)

class RoadmapGenerator:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

    def enhance_roadmap(self, parsed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Улучшает спарсенные данные с помощью GPT:
        - Добавляет описания
        - Уточняет материалы
        - Оптимизирует структуру
        """
        prompt = self._build_enhancement_prompt(parsed_data)

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Ты — помощник для создания учебных роадмапов. "
                            "Улучши структуру курса на основе предоставленных данных. "
                            "Добавь описания, рекомендуемые материалы и оптимизируй зависимости."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format={"type": "json_object"},
                temperature=0.5,
                max_tokens=2000
            )

            return json.loads(response.choices[0].message.content)

        except Exception as e:
            logger.error(f"Ошибка OpenAI API: {str(e)}")
            raise RoadmapGenerationError(f"Ошибка улучшения роадмапа: {str(e)}")

    def _build_enhancement_prompt(self, data: Dict[str, Any]) -> str:
        """Создает промпт для улучшения спарсенных данных"""
        return f"""
        Проанализируй структуру курса и улучши её, следуя инструкциям:
        
        1. Для каждой темы и подтемы добавь подробное описание (2-3 предложения)
        2. Для каждого материала укажи подходящий тип (video/article/assignment)
        3. Добавь рекомендуемые URL для материалов (если уместно)
        4. Оптимизируй зависимости между темами
        5. Сохрани исходную структуру и порядок
        
        Исходные данные:
        {json.dumps(data, ensure_ascii=False, indent=2)}
        
        Формат ответа (JSON):
        {{
            "topics": [
                {{
                    "title": "Название",
                    "description": "Описание",
                    "order": 1,
                    "subtopics": [
                        {{
                            "title": "Название",
                            "description": "Описание",
                            "order": 1
                        }}
                    ]
                }}
            ],
            "dependencies": [
                {{
                    "from": "Тема A",
                    "to": "Тема B"
                }}
            ],
            "materials": [
                {{
                    "topic": "Тема",
                    "type": "video/article/assignment",
                    "title": "Название",
                    "url": "Ссылка",
                    "content": "Описание"
                }}
            ]
        }}
        """

class RoadmapGenerationError(Exception):
    pass