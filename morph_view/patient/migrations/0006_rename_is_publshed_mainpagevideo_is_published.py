# Generated by Django 4.0.4 on 2023-03-11 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_mainpagevideo_is_publshed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainpagevideo',
            old_name='is_publshed',
            new_name='is_published',
        ),
    ]
