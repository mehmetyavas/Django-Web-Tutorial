# Generated by Django 4.0.6 on 2022-07-17 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_order_rename_products_item_delete_cart_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='urun_fiyat',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='urun_adi',
            new_name='title',
        ),
    ]
