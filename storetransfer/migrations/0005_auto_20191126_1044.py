# Generated by Django 2.2.6 on 2019-11-26 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storetransfer', '0004_inventoryitem_inventoryitemupc_inventoryitemupctype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='inventory_item_sku_MPQ',
            new_name='inventory_item_MPQ',
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='inventory_item_sku_case_cost',
            new_name='inventory_item_case_cost',
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='inventory_item_sku_category',
            new_name='inventory_item_category',
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='inventory_item_sku_distributor',
            new_name='inventory_item_distributor',
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='inventory_item_sku_name',
            new_name='inventory_item_name',
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='inventory_item_sku_size',
            new_name='inventory_item_size',
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='inventory_item_sku_sku',
            new_name='inventory_item_sku',
        ),
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='inventory_item_sku_split_bottle_cost',
            new_name='inventory_item_split_bottle_cost',
        ),
    ]
