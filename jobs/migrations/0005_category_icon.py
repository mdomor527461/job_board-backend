# Generated by Django 5.1.2 on 2024-10-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_jobapplication_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
