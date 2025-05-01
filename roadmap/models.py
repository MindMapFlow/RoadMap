from django.db import models
from django.core.exceptions import ValidationError

class Syllabus(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(blank=True, null=True, verbose_name="Содержание")
    file = models.FileField(
        upload_to='syllabus_files/',
        blank=True,
        null=True,
        verbose_name="Файл силлабуса"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Силлабус"
        verbose_name_plural = "Силлабусы"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Topic(models.Model):
    syllabus = models.ForeignKey(
        Syllabus,
        related_name='topics',
        on_delete=models.CASCADE,
        verbose_name="Силлабус"
    )
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subtopics',
        on_delete=models.CASCADE,
        verbose_name="Родительская тема"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        ordering = ['order']
        indexes = [
            models.Index(fields=['syllabus', 'order']),
        ]

    def __str__(self):
        return f"{self.title} (Порядок: {self.order})"

class Material(models.Model):
    MATERIAL_TYPES = [
        ('video', 'Видео'),
        ('article', 'Статья'),
        ('assignment', 'Задание'),
    ]

    topic = models.ForeignKey(
        Topic,
        related_name='materials',
        on_delete=models.CASCADE,
        verbose_name="Тема"
    )
    material_type = models.CharField(
        max_length=50,
        choices=MATERIAL_TYPES,
        verbose_name="Тип материала"
    )
    title = models.CharField(max_length=255, verbose_name="Название")
    url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    content = models.TextField(blank=True, null=True, verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_material_type_display()}: {self.title}"

class TopicDependency(models.Model):
    from_topic = models.ForeignKey(
        Topic,
        related_name='dependencies_from',
        on_delete=models.CASCADE,
        verbose_name="Исходная тема"
    )
    to_topic = models.ForeignKey(
        Topic,
        related_name='dependencies_to',
        on_delete=models.CASCADE,
        verbose_name="Целевая тема"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Зависимость тем"
        verbose_name_plural = "Зависимости тем"
        unique_together = ('from_topic', 'to_topic')

    def clean(self):
        if self.from_topic == self.to_topic:
            raise ValidationError("Тема не может зависеть от самой себя")
        if self.from_topic.syllabus != self.to_topic.syllabus:
            raise ValidationError("Зависимости возможны только в рамках одного силлабуса")

    def __str__(self):
        return f"{self.from_topic} → {self.to_topic}"