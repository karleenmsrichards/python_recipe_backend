# Generated by Django 4.2.11 on 2024-04-06 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_recipe_uri'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='total_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='uri',
        ),
    ]
