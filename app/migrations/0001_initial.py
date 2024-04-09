# Generated by Django 4.2.11 on 2024-04-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.URLField(max_length=1000)),
                ('ingredients', models.TextField()),
                ('diet_labels', models.CharField(blank=True, max_length=100, null=True)),
                ('health_labels', models.CharField(blank=True, max_length=200, null=True)),
                ('cautions', models.CharField(blank=True, max_length=100, null=True)),
                ('calories', models.FloatField(blank=True, null=True)),
                ('total_time', models.IntegerField(blank=True, null=True)),
                ('meal_type', models.CharField(blank=True, max_length=50, null=True)),
                ('yield_amount', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
    ]
