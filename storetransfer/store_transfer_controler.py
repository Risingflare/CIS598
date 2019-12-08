import pandas as pd

def StoreTransfer_start(store_name, csv_file):
    print(store_name)
    ReadFile(csv_file)


def ReadFile(csv_file):
    inventory_df = pd.read_csv(csv_file)
    count = 0
    for index, item in inventory_df.iterrows():
        if count < 10:
            item_name = item["Item Name"]
            sku = item["SKU"]
            upc = item["UPC"]
            distributor = item["Distributor"]
            size = item["Size"]
            category = item["Category"]
            case_cost = item["Case Cost"]
            split_bottle_cost = item["Split Bottle Cost"]
            retail_price = item["Retail Price"]
            mpq = item["MPQ"]
            on_hand_count = item["On Hand Count"]
            print('{} {} {} {} {} {} {} {} {} {} {}'.format(item_name, sku, upc, distributor, size, category, case_cost, split_bottle_cost, retail_price, mpq, on_hand_count))
            count+=1
        else:
            break
    print(inventory_df.head(2))