# Generated by Django 5.2.4 on 2025-07-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_blogpost_preview_image_alter_exhibition_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
