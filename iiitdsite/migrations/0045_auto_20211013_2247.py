# Generated by Django 3.2.6 on 2021-10-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0044_tenders_tender_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenders',
            name='tender_title',
        ),
        migrations.AlterField(
            model_name='tenders',
            name='publishedDate',
            field=models.DateField(),
        ),
    ]
