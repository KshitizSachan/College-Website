# Generated by Django 3.2.6 on 2021-10-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0055_auto_20211017_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='form',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
