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
        fields = '__all__'
    
class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'
    
class InventoryItemUPCForm(forms.ModelForm):
    class Meta:
        model = InventoryItemUPC
        fields = '__all__'
