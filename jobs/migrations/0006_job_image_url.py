# Generated by Django 5.1.2 on 2024-10-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]