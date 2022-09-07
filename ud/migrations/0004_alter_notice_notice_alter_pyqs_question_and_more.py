# Generated by Django 4.0.4 on 2022-05-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ud', '0003_alter_notice_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice',
            field=models.FileField(blank=True, upload_to='media/notice'),
        ),
        migrations.AlterField(
            model_name='pyqs',
            name='question',
            field=models.FileField(blank=True, upload_to='media/pyqs'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(upload_to='media/resume'),
        ),
    ]
