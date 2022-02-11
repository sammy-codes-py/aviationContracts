# Generated by Django 4.0.2 on 2022-02-08 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_seekerprofile_is_open_to_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerprofile',
            name='cv',
            field=models.FileField(blank=True, upload_to='seeker/cv', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]),
        ),
    ]
