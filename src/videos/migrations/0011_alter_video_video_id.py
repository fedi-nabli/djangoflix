# Generated by Django 3.2.16 on 2023-01-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_auto_20230108_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]
