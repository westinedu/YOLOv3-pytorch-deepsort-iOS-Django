# Generated by Django 2.1.1 on 2019-05-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_media_object_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='finishied',
        ),
        migrations.AddField(
            model_name='media',
            name='finished',
            field=models.BooleanField(default=True),
        ),
    ]
