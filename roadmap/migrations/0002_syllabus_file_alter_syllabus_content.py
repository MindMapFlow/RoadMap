# Generated by Django 5.2 on 2025-05-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='syllabus_files/'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
