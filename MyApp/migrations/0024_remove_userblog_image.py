# Generated by Django 3.0.4 on 2020-06-25 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0023_auto_20200625_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userblog',
            name='image',
        ),
    ]
