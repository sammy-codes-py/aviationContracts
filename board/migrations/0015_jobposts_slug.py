# Generated by Django 4.0.2 on 2022-02-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_recruiterprofile_available_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposts',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
