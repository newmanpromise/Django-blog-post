# Generated by Django 5.0 on 2024-02-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click the link above to read blog post', max_length=255),
        ),
    ]