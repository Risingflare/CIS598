from .models import *
import decimal

def Store_creation_start(store_id, item_id_list, markup_percent):
    for item_id in item_id_list:
        inventory_item = InventoryItem.objects.get(id=item_id)
        base_cost = inventory_item.inventory_item_case_cost/inventory_item.inventory_item_MPQ
        retail_price = base_cost * decimal.Decimal((1+markup_percent))
        retail_price = round(retail_price,2)
        Item.objects.get_or_create(
            store_id=store_id,
            item_sku=inventory_item.inventory_item_sku,
            item_upc=inventory_item.inventory_item_upc,
            item_distributor_id=inventory_item.inventory_item_distributor_id,
            item_size_id=inventory_item.inventory_item_size_id,
            item_category_id=inventory_item.inventory_item_category_id,
            item_name=inventory_item.inventory_item_name,
            item_case_cost=inventory_item.inventory_item_case_cost,
            item_split_bottle_cost=inventory_item.inventory_item_split_bottle_cost,
            item_retail_price=retail_price,
            item_MPQ=inventory_item.inventory_item_MPQ,
            item_on_hand_count=0,
            item_error_value=False
        )