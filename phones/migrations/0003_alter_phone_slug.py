# Generated by Django 3.2.4 on 2021-06-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(verbose_name='URL'),
        ),
    ]