# Generated by Django 3.2.6 on 2021-10-10 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0039_updates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='description_hindi',
        ),
        migrations.RemoveField(
            model_name='events',
            name='description_kannada',
        ),
        migrations.RemoveField(
            model_name='events',
            name='event_name_hindi',
        ),
        migrations.RemoveField(
            model_name='events',
            name='event_name_kannada',
        ),
    ]
