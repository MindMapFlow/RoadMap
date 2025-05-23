# Generated by Django 5.2 on 2025-05-01 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0005_alter_material_options_alter_syllabus_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['-created_at'], 'verbose_name': 'Материал', 'verbose_name_plural': 'Материалы'},
        ),
        migrations.AlterModelOptions(
            name='syllabus',
            options={'ordering': ['-created_at'], 'verbose_name': 'Силлабус', 'verbose_name_plural': 'Силлабусы'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['order'], 'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterModelOptions(
            name='topicdependency',
            options={'verbose_name': 'Зависимость тем', 'verbose_name_plural': 'Зависимости тем'},
        ),
        migrations.AlterField(
            model_name='material',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='material',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_type',
            field=models.CharField(choices=[('video', 'Видео'), ('article', 'Статья'), ('assignment', 'Задание')], max_length=50, verbose_name='Тип материала'),
        ),
        migrations.AlterField(
            model_name='material',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='material',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='roadmap.topic', verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='material',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='syllabus_files/', verbose_name='Файл силлабуса'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtopics', to='roadmap.topic', verbose_name='Родительская тема'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='roadmap.syllabus', verbose_name='Силлабус'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='topicdependency',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='topicdependency',
            name='from_topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependencies_from', to='roadmap.topic', verbose_name='Исходная тема'),
        ),
        migrations.AlterField(
            model_name='topicdependency',
            name='to_topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependencies_to', to='roadmap.topic', verbose_name='Целевая тема'),
        ),
    ]
