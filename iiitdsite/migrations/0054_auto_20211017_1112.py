# Generated by Django 3.2.6 on 2021-10-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iiitdsite', '0053_merge_0052_clubs_mail_0052_magazine_team_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='Formlink',
        ),
        migrations.RemoveField(
            model_name='tenders',
            name='tender_document',
        ),
        migrations.AddField(
            model_name='jobs',
            name='form',
            field=models.FileField(blank=True, null=True, upload_to='Magazine/Jobs/'),
        ),
        migrations.AddField(
            model_name='magazine_issues',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Magazine/Issues/'),
        ),
        migrations.AddField(
            model_name='tenders',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Magazine/Tenders/'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='instructions',
            field=models.FileField(blank=True, null=True, upload_to='Magazine/Jobs/'),
        ),
    ]
