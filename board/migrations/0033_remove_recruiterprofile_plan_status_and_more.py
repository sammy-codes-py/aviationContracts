# Generated by Django 4.0.2 on 2022-02-22 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0032_recruiterprofile_plan_end_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiterprofile',
            name='plan_status',
        ),
        migrations.RemoveField(
            model_name='recruiterprofile',
            name='stripe_customer_id',
        ),
        migrations.RemoveField(
            model_name='recruiterprofile',
            name='stripe_subscription_id',
        ),
    ]