# Generated by Django 5.1.7 on 2025-04-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hom', '0003_live_index_history_img_live_index_history_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_title', models.CharField(max_length=120, null=True)),
                ('history_img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='uploads/history/')),
            ],
        ),
        migrations.RemoveField(
            model_name='live_index',
            name='history_img',
        ),
        migrations.RemoveField(
            model_name='live_index',
            name='history_title',
        ),
    ]
