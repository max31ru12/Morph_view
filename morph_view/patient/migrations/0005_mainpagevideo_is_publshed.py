# Generated by Django 4.0.4 on 2023-03-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_mainpagevideo_video_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpagevideo',
            name='is_publshed',
            field=models.BooleanField(default=False),
        ),
    ]
