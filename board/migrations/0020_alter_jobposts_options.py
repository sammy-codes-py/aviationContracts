# Generated by Django 4.0.2 on 2022-02-15 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0019_alter_jobposts_post_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobposts',
            options={'ordering': ('post_date',)},
        ),
    ]