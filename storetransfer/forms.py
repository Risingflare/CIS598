from django import forms

from .models import *

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class DistributorForm(forms.ModelForm):
    class Meta:
        model = Distributor
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'store','item_sku','item_upc','item_distributor','item_size','item_category','item_name','item_case_cost',
            'item_split_bottle_cost','item_retail_price','item_MPQ','item_on_hand_count'
        ]
    
class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'
    
class StoreTransferForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['store_name']
