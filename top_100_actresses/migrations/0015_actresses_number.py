# Generated by Django 5.0.3 on 2024-07-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_100_actresses', '0014_actresses_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='actresses',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
