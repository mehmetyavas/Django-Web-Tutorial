# Generated by Django 4.0.6 on 2022-07-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_hakkimizda_ilesitim'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilesitim',
            name='address',
            field=models.CharField(max_length=300, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='ilesitim',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='ilesitim',
            name='icon',
            field=models.CharField(max_length=200, null=True, verbose_name='İKON'),
        ),
        migrations.AddField(
            model_name='ilesitim',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
