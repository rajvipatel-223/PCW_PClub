# Generated by Django 3.0.4 on 2020-06-22 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_auto_20200622_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='title',
        ),
    ]
