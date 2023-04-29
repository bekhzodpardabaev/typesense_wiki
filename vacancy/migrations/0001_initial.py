# Generated by Django 3.2.13 on 2023-01-27 07:13

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('search_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('salary', models.IntegerField()),
                ('location_lat', models.FloatField()),
                ('location_lon', models.FloatField()),
                ('search_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.category')),
            ],
        ),
    ]
