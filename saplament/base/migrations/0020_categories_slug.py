# Generated by Django 4.0.6 on 2022-07-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_delete_footerurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]