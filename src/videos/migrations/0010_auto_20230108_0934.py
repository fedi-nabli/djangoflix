# Generated by Django 3.2.16 on 2023-01-08 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_alter_video_publish_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
