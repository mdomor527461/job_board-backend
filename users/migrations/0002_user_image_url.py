# Generated by Django 5.1.2 on 2024-10-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
