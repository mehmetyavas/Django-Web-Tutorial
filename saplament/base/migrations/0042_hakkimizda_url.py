# Generated by Django 4.0.6 on 2022-07-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_hakkimizda_field_hakkimizda_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hakkimizda',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
