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

class StoreTransferForm(forms.Form):
    choices = [('EzSpirits','EzSpirits'),('EzForYou','EzForYou'),('CSV','CSV')]
    store_name = forms.CharField(max_length=50)
    Options = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    def clean_store_name(self):
        store_name = self.cleaned_data['store_name']
        if Store.objects.filter(store_name=store_name).exists():
            raise forms.ValidationError("Store Name already exists.")
        return store_name