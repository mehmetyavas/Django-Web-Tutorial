# Generated by Django 4.0.6 on 2022-07-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0049_remove_products_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerurl',
            name='deneme',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
