# Generated by Django 5.1.7 on 2025-04-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Live_index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=10000)),
                ('img_about', models.ImageField(upload_to='media')),
            ],
        ),
    ]
