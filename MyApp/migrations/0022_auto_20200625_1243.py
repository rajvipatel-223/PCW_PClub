# Generated by Django 3.0.4 on 2020-06-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0021_user_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_blog',
            name='user_emailId',
            field=models.EmailField(max_length=50),
        ),
    ]
