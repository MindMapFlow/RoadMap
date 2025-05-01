from rest_framework import generics, status
from django.http import JsonResponse
from .models import Syllabus, Topic, Material, TopicDependency
from .serializers import SyllabusSerializer
from .services import RoadmapGenerator
from .utils import parse_syllabus, extract_text_from_docx
import logging
from django.db import transaction
from django.db.models import Max

logger = logging.getLogger(__name__)

class SyllabusListCreateView(generics.ListCreateAPIView):
    queryset = Syllabus.objects.all().prefetch_related(
        'topics',
        'topics__subtopics',
        'topics__materials',
        'topics__dependencies_from',
        'topics__dependencies_to'
    )
    serializer_class = SyllabusSerializer

class SyllabusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Syllabus.objects.all().prefetch_related(
        'topics',
        'topics__subtopics',
        'topics__materials',
        'topics__dependencies_from',
        'topics__dependencies_to'
    )
    serializer_class = SyllabusSerializer

def generate_roadmap(request, syllabus_id):
    try:
        syllabus = Syllabus.objects.get(pk=syllabus_id)

        # Извлекаем контент
        content = (
            extract_text_from_docx(syllabus.file.path)
            if syllabus.file else
            syllabus.content
        )

        if not content:
            return JsonResponse(
                {"error": "Силлабус не содержит данных для анализа"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Парсим базовую структуру
        parsed_data = parse_syllabus(content)

        # Улучшаем структуру с помощью GPT
        generator = RoadmapGenerator()
        roadmap_data = generator.enhance_roadmap(parsed_data)

        # Удаляем старые данные в транзакции
        with transaction.atomic():
            syllabus.topics.all().delete()

            topic_map = {}
            for topic_data in roadmap_data["topics"]:
                # Ищем максимальный order и добавляем 1
                max_order = Topic.objects.filter(syllabus=syllabus).aggregate(Max('order'))['order__max'] or 0
                topic = Topic.objects.create(
                    syllabus=syllabus,
                    title=topic_data["title"],
                    description=topic_data["description"],
                    order=max_order + 1
                )
                topic_map[topic_data["title"]] = topic

                for subtopic_data in topic_data.get("subtopics", []):
                    subtopic = Topic.objects.create(
                        syllabus=syllabus,
                        title=subtopic_data["title"],
                        description=subtopic_data["description"],
                        order=len(topic.subtopics.all()) + 1,
                        parent=topic
                    )
                    topic_map[subtopic_data["title"]] = subtopic

            # Сохраняем зависимости
            for dep in roadmap_data["dependencies"]:
                TopicDependency.objects.create(
                    from_topic=topic_map[dep["from"]],
                    to_topic=topic_map[dep["to"]]
                )

            # Сохраняем материалы
            for material_data in roadmap_data["materials"]:
                Material.objects.create(
                    topic=topic_map[material_data["topic"]],
                    material_type=material_data["type"],
                    title=material_data["title"],
                    url=material_data.get("url", ""),
                    content=material_data.get("content", "")
                )

        return JsonResponse({
            "status": "success",
            "roadmap": roadmap_data
        })

    except Syllabus.DoesNotExist:
        return JsonResponse(
            {"error": "Силлабус не найден"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        logger.exception("Ошибка при генерации роадмапа")
        return JsonResponse(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )