# Generated by Django 4.2.11 on 2024-04-06 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='thumbnail',
            new_name='image',
        ),
    ]
