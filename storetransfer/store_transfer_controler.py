import pandas as pd
from difflib import SequenceMatcher
from .models import *

# Using the sequence matcher from difflib this returns the ratio of similarities between both parameter strings
def similar(string_a, string_b):
    return SequenceMatcher(None, string_a, string_b).ratio()

# Start the file transfer process
def StoreTransfer_start(store_name, csv_file):
    print(store_name) # create store
    #store_id = Store_create(store_name)
    ReadFile(csv_file, 1)

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
    count = 0
    for index, item in inventory_df.iterrows():
        try:
            if count < 10:
                item_name = item["Item Name"]
                sku = item["Product SKU"]
                distributor = item["Distributor"]
                if not item_name == '' and not sku == '' and not distributor == '':
                    distributor_id = GetDistributorPK(distributor, distributor_dictionary)
                    #Finish_item(item_name, sku, distributor, item, store_id)
                elif not distributor == '' and not item_name == '':
                    pass
                elif not distributor == '' and not sku == '':
                    pass
                elif not item_name == '' and not sku == '':
                    pass
                else:
                    continue
                count+=1
            else:
                break
        except KeyError as exception:
           column_error = exception.args
           # Delete store
           raise KeyError("%s column is incorrect in the CSV file" % column_error)

def Finish_item(item_name, sku, distributor, item, store_id):
    upc = item["Item Number"]
    size = item["Size"]
    category = item["Category"]
    case_cost = item["Case Cost"]
    split_bottle_cost = item["Single Bottle Cost"]
    retail_price = item["Retail Price"]
    mpq = item["Quantity Case"]
    on_hand_count = item["Quantity on Hand"]
    print('{} {} {} {} {} {} {} {} {} {} {}'.format(item_name, sku, upc, distributor, size, category, case_cost, split_bottle_cost, retail_price, mpq, on_hand_count))

def GetDistributorPK(distributor, distributor_dictionary):
    if distributor in distributor_dictionary:
        return distributor_dictionary[distributor]
    else:
        distributor_list = Distributor.objects.filter(distributor_name__startswith=distributor[0])
        for distributor_item in distributor_list:
            ratio = similar(distributor.lower(), distributor_item.distributor_name.lower())
            if ratio >= 0.65:
                print(distributor_item.id)
                distributor_dictionary[distributor] = distributor_item.id
                return distributor_item.id
        # Create new distributor
        database_distributor = Distributor(distributor_name=distributor)
        database_distributor.save()
        distributor_dictionary[distributor] = database_distributor.id
        return database_distributor.id


def Get_SKU(distributor, item_name):
    pass