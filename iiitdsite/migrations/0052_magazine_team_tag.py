# Generated by Django 3.2.6 on 2021-10-16 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0051_auto_20211017_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine_team',
            name='tag',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
