# Generated by Django 4.0.6 on 2022-07-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_hakkimizda_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hakkimizda',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
