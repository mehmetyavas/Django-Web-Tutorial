# Generated by Django 4.0.6 on 2022-07-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_remove_ilesitim_address_remove_ilesitim_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilesitim',
            name='name',
            field=models.CharField(max_length=300, null=True, verbose_name='Alan'),
        ),
    ]
