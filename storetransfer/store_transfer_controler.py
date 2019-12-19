import pandas as pd
from difflib import SequenceMatcher
from .models import *

# Using the sequence matcher from difflib this returns the ratio of similarities between both parameter strings
def similar(string_a, string_b):
    return SequenceMatcher(None, string_a, string_b).ratio()

# Start the file transfer process
def StoreTransfer_start(store_name, csv_file):
    store_id = Store_create(store_name)
    ReadFile(csv_file, store_id)
    return store_id

# Create the new store in the database and return the PK
def Store_create(store_name):
    store = Store(store_name=store_name)
    store.save()
    return store.id

# Begin reading the file. If the item does not have the correct Column titles a KeyError will be thrown
def ReadFile(csv_file, store_id):
    inventory_df = pd.read_csv(csv_file)
    inventory_df = inventory_df.fillna('') # Change all NaN values to an empty string
    distributor_dictionary = {} # This dictionary will be used to keep track of the foreign keys for distributors in the csv file, to save time.
    category_dictionary = {}
    size_dictionary = {}
    for index, item in inventory_df.iterrows():
        try:
            item_name = item["Item Name"]
            sku = item["Product SKU"]
            if str(sku).isdigit():
                sku = int(sku)
            else:
                sku = ''
            upc = item["Item Number"]
            if str(upc).isdigit():
                upc = int(upc)
            else:
                upc = ''
            distributor = item["Distributor"]
            distributor_id = None
            if not distributor == '':
                distributor_id = GetDistributorPK(distributor, distributor_dictionary)
                inventory_item_db = GetInventoryItem(distributor_id, sku, upc)
            if not item_name == '' and not sku == '' and not distributor == '':
                Finish_item(item_name, sku, distributor_id, upc, category_dictionary, size_dictionary, item, store_id, inventory_item_db)
            elif not distributor == '' and not item_name == '':
                if inventory_item_db:
                    sku = inventory_item_db.inventory_item_sku
                    Finish_item(item_name, sku, distributor_id, upc, category_dictionary, size_dictionary, item, store_id, inventory_item_db)
            elif not distributor == '' and not sku == '':
                if inventory_item_db:
                    item_name = inventory_item_db.inventory_item_name
                    Finish_item(item_name, sku, distributor_id, upc, category_dictionary, size_dictionary, item, store_id, inventory_item_db)
            else:
                continue
        except KeyError as exception:
            column_error = exception.args
            raise KeyError("%s column is incorrect in the CSV file" % column_error)

def Finish_item(item_name, sku, distributor_id, upc, category_dictionary, size_dictionary, item, store_id, inventory_item_db):
    item_error_value = False
    if inventory_item_db:
        create_inventory_item_boolean = False
    else:
        create_inventory_item_boolean = True
    category = item["Category"]
    if not category == '':
        category_id = GetCategoryPK(category, category_dictionary)
    elif inventory_item_db:
        category_id = inventory_item_db.inventory_item_category
    else:
        category_id = None
        create_inventory_item_boolean = False
    size = item["Size"]
    if not size == '':
        size_id = GetSizePK(size, size_dictionary)
    elif inventory_item_db:
        size_id = inventory_item_db.inventory_item_size
    else:
        size_id = None
        create_inventory_item_boolean = False
        item_error_value = True
    if upc == '':
        if inventory_item_db:
            upc = inventory_item_db.inventory_item_upc
        else:
            item_error_value = True
            create_inventory_item_boolean = False
            upc = -1
    case_cost = item["Case Cost"]
    if case_cost == '':
        if inventory_item_db:
            case_cost = inventory_item_db.inventory_item_case_cost
        else:
            item_error_value = True
            create_inventory_item_boolean = False
            case_cost = -1
    split_bottle_cost = item["Single Bottle Cost"]
    if split_bottle_cost == '':
        if inventory_item_db:
            split_bottle_cost = inventory_item_db.inventory_item_split_bottle_cost
        else:
            item_error_value = True
            create_inventory_item_boolean = False
            split_bottle_cost = -1
    retail_price = item["Retail Price"]
    if retail_price == '':
        item_error_value = True
        retail_price = -1
    mpq = item["Quantity Case"]
    if mpq == '':
        if inventory_item_db:
            mpq = inventory_item_db.inventory_item_MPQ
        else:
            item_error_value = True
            create_inventory_item_boolean = False
            mpq = -1
    on_hand_count = item["Quantity on Hand"]
    if on_hand_count == '':
        item_error_value = True
        on_hand_count = -1
    # Create item
    CreateStoreItem(store_id, sku, upc, distributor_id, size_id, category_id, item_name, case_cost, split_bottle_cost, retail_price, mpq, on_hand_count, item_error_value)
    if create_inventory_item_boolean == True:
        # Create Inventory Item
        CreateInventoryItemDB(sku, int(upc), distributor_id, size_id, category_id, item_name, case_cost, split_bottle_cost, mpq)

# Get the ditributor primary key.
# First check dictionary, 
# if not there check database, 
# if not there create new distributor in DB and store key in dictionary
def GetDistributorPK(distributor, distributor_dictionary):
    if distributor in distributor_dictionary:
        return distributor_dictionary[distributor]
    else:
        distributor_list = Distributor.objects.filter(distributor_name__startswith=distributor[0])
        for distributor_item in distributor_list:
            ratio = similar(distributor.lower(), distributor_item.distributor_name.lower())
            if ratio >= 0.65:
                distributor_dictionary[distributor] = distributor_item.id
                return distributor_item.id
        # Create new distributor
        database_distributor = Distributor(distributor_name=distributor)
        database_distributor.save()
        distributor_dictionary[distributor] = database_distributor.id
        return database_distributor.id

# Get the Category primary key.
# First check dictionary, 
# if not there check database, 
# if not there create new category in DB and store key in dictionary
def GetCategoryPK(category, category_dictionary):
    if category in category_dictionary:
        return category_dictionary[category]
    else:
        category_list = Category.objects.filter(category_name__startswith=category[0])
        for category_item in category_list:
            ratio = similar(category.lower(), category_item.category_name.lower())
            if ratio >= 0.65:
                category_dictionary[category] = category_item.id
                return category_item.id
        database_category = Category(category_name=category)
        database_category.save()
        category_dictionary[category] = database_category.id
        return database_category.id

# Get the Size primary key.
# First check dictionary, 
# if not there check database, 
# if not there create new Size in DB and store key in dictionary
def GetSizePK(size, size_dictionary):
    if size in size_dictionary:
        return size_dictionary[size]
    else:
        size_list = Size.objects.filter(size_name__startswith=size[0])
        for size_item in size_list:
            ratio = similar(size.lower(), size_item.size_name.lower())
            if ratio >= 0.65:
                size_dictionary[size] = size_item.id
                return size_item.id
        database_size = Size(size_name=size)
        database_size.save()
        size_dictionary[size] = database_size.id
        return database_size.id


def GetInventoryItem(distributor_id, sku, upc):
    try:
        if not sku == '' and not upc == '':
            return InventoryItem.objects.get(inventory_item_distributor=distributor_id, inventory_item_sku=sku, inventory_item_upc=upc)
        elif not sku == '':
            return InventoryItem.objects.get(inventory_item_distributor=distributor_id, inventory_item_sku=sku)
        elif not upc == '':
            return InventoryItem.objects.get(inventory_item_distributor=distributor_id, inventory_item_upc=upc)
        else:
            return None
    except InventoryItem.DoesNotExist:
        return None

def CreateStoreItem(store_id, sku, upc, distributor_id, size_id, category_id, item_name, case_cost, split_bottle_cost, retail_price, mpq, on_hand_count, item_error_value):
    Item.objects.get_or_create(
            store_id=store_id,
            item_sku=sku,
            item_upc=upc,
            item_distributor_id=distributor_id,
            item_size_id=size_id,
            item_category_id=category_id,
            item_name=item_name,
            item_case_cost=case_cost,
            item_split_bottle_cost=split_bottle_cost,
            item_retail_price=retail_price,
            item_MPQ=mpq,
            item_on_hand_count=on_hand_count,
            item_error_value=item_error_value
    )

def CreateInventoryItemDB(sku, upc, distributor_id, size_id, category_id, item_name, case_cost, split_bottle_cost, mpq):
    InventoryItem.objects.get_or_create(
        inventory_item_sku=sku,
        inventory_item_upc=upc,
        inventory_item_distributor_id=distributor_id,
        inventory_item_size_id=size_id,
        inventory_item_category_id=category_id,
        inventory_item_name=item_name,
        inventory_item_case_cost=case_cost,
        inventory_item_split_bottle_cost=split_bottle_cost,
        inventory_item_MPQ=mpq
    )