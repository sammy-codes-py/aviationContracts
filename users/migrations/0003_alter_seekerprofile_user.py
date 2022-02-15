# Generated by Django 4.0.2 on 2022-02-13 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_seekerprofile_recruiterprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
