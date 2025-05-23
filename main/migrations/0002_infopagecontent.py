# Generated by Django 5.1.5 on 2025-03-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portrait', models.ImageField(blank=True, null=True, upload_to='info/')),
                ('bio', models.TextField(help_text='Nadia-Lin’s bio or artist statement')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Info Page Content',
                'verbose_name_plural': 'Info Page Content',
            },
        ),
    ]
