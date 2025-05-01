from rest_framework import serializers
from .models import Syllabus, Topic, TopicDependency, Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'title', 'material_type', 'url', 'content', 'created_at']

class TopicDependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicDependency
        fields = ['id', 'from_topic', 'to_topic', 'created_at']

class TopicSerializer(serializers.ModelSerializer):
    subtopics = serializers.SerializerMethodField()
    materials = MaterialSerializer(many=True, read_only=True)
    dependencies_from = TopicDependencySerializer(many=True, read_only=True)
    dependencies_to = TopicDependencySerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = [
            'id', 'title', 'description', 'order',
            'subtopics', 'materials',
            'dependencies_from', 'dependencies_to',
            'created_at'
        ]

    def get_subtopics(self, obj):
        subtopics = obj.subtopics.all().order_by('order')
        return TopicSerializer(subtopics, many=True).data

class SyllabusSerializer(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField()

    class Meta:
        model = Syllabus
        fields = ['id', 'title', 'content', 'file', 'topics', 'created_at']

    def get_topics(self, obj):
        topics = obj.topics.filter(parent__isnull=True).order_by('order')
        return TopicSerializer(topics, many=True).data