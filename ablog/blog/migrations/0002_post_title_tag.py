# Generated by Django 5.0 on 2023-12-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=" Newman's Blog", max_length=255),
        ),
    ]
