# Generated by Django 5.1.2 on 2024-10-23 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_jobapplication_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='resume',
        ),
    ]
