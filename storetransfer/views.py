from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from .store_transfer_controler import StoreTransfer_start

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

# Store create view
def store_create_view(request):
    form = StoreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "store/store_create.html", context)

# Store update view
def store_update_view(request, id):
    obj = get_object_or_404(Store, id=id)
    form = StoreForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "store/store_create.html", context)

def store_list_view(request):
    queryset = Store.objects.all()
    count = len(queryset)
    context = {
        "object_list": queryset,
        "count": count
    }
    return render(request, "store/store_list.html", context)

def store_detail_view(request, id):
    obj = get_object_or_404(Store, id=id)
    object_list = Item.objects.filter(store=id)
    count = len(object_list)
    context = {
        "object":obj,
        "object_list": object_list,
        "count": count
    }
    return render(request, "store/store_detail.html", context)

def store_delete_view(request, id):
    obj = get_object_or_404(Store, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "store/store_delete.html", context)

def distributor_create_view(request):
    form = DistributorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "distributor/distributor_create.html", context)

def distributor_update_view(request, id):
    obj = get_object_or_404(Distributor, id=id)
    form = DistributorForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "distributor/distributor_create.html", context)

def distributor_list_view(request):
    queryset = Distributor.objects.all()
    count = len(queryset)
    context = {
        "object_list": queryset,
        "count": count
    }
    return render(request, "distributor/distributor_list.html", context)

def distributor_detail_view(request, id):
    obj = get_object_or_404(Distributor, id=id)
    context = {
        "object":obj
    }
    return render(request, "distributor/distributor_detail.html", context)

def distributor_delete_view(request, id):
    obj = get_object_or_404(Distributor, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "distributor/distributor_delete.html", context)

def category_create_view(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "category/category_create.html", context)

def category_update_view(request, id):
    obj = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "category/category_create.html", context)

def category_list_view(request):
    queryset = Category.objects.all()
    count = len(queryset)
    context = {
        "object_list": queryset,
        "count": count
    }
    return render(request, "category/category_list.html", context)

def category_delete_view(request, id):
    obj = get_object_or_404(Category, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "category/category_delete.html", context)

def category_detail_view(request, id):
    obj = get_object_or_404(Category, id=id)
    context = {
        "object":obj
    }
    return render(request, "category/category_detail.html", context)

def size_create_view(request):
    form = SizeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "size/size_create.html", context)

def size_update_view(request, id):
    obj = get_object_or_404(Size, id=id)
    form = SizeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "size/size_create.html", context)

def size_list_view(request):
    queryset = Size.objects.all()
    count = len(queryset)
    context = {
        "object_list": queryset,
        "count": count
    }
    return render(request, "size/size_list.html", context)

def size_delete_view(request, id):
    obj = get_object_or_404(Size, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "size/size_delete.html", context)

def size_detail_view(request, id):
    obj = get_object_or_404(Size, id=id)
    context = {
        "object":obj
    }
    return render(request, "size/size_detail.html", context)

def inventory_item_create_view(request):
    form = InventoryItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InventoryItemForm()
    context = {
        'form': form
    }
    return render(request, "inventory_item/inventory_item_create.html", context)

def inventory_item_update_view(request, id):
    obj = get_object_or_404(InventoryItem, id=id)
    form = InventoryItemForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "inventory_item/inventory_item_create.html", context)

def inventory_item_list_view(request):
    queryset = InventoryItem.objects.all()
    count = len(queryset)
    context = {
        "object_list": queryset,
        "count": count
    }
    return render(request, "inventory_item/inventory_item_list.html", context)

def inventory_item_detail_view(request, id):
    obj = get_object_or_404(InventoryItem, id=id)
    object_list = InventoryItemUPC.objects.filter(inventory_item=id)
    count = len(object_list)
    context = {
        "object":obj,
        "object_list":object_list,
        "count":count
    }
    return render(request, "inventory_item/inventory_item_detail.html", context)

def inventory_item_delete_view(request, id):
    obj = get_object_or_404(InventoryItem, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "inventory_item/inventory_item_delete.html", context)

def item_create_view(request, store_id):
    form = ItemForm(request.POST or None, initial={'store':store_id})
    if form.is_valid():
        form.save()
        form = ItemForm(initial={'store':store_id})
    context = {
        'form': form
    }
    return render(request, "item/item_create.html", context)

def item_update_view(request, store_id, id):
    obj = get_object_or_404(Item, store=store_id, id=id)
    form = ItemForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "item/item_create.html", context)

def item_detail_view(request, store_id, id):
    obj = get_object_or_404(Item, store=store_id, id=id)
    context = {
        "object":obj
    }
    return render(request, "item/item_detail.html", context)

def item_delete_view(request, store_id, id):
    obj = get_object_or_404(Item, store=store_id, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        "object": obj
    }
    return render(request, "item/item_delete.html", context)

def inventory_item_upc_create_view(request, inventory_item_id):
    form = InventoryItemUPCForm(request.POST or None, initial={'inventory_item':inventory_item_id})
    if form.is_valid():
        form.save()
        form = InventoryItemUPCForm(initial={'inventory_item':inventory_item_id})
    context = {
        'form': form
    }
    return render(request, "inventory_item_upc/inventory_item_upc_create.html", context)

def inventory_item_upc_update_view(request, inventory_item_id, id):
    obj = get_object_or_404(InventoryItemUPC, inventory_item=inventory_item_id, id=id)
    form = InventoryItemUPCForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "inventory_item_upc/inventory_item_upc_create.html", context)

def inventory_item_upc_detail_view(request, inventory_item_id, id):
    obj = get_object_or_404(InventoryItemUPC, inventory_item=inventory_item_id, id=id)
    context = {
        "object":obj
    }
    return render(request, "inventory_item_upc/inventory_item_upc_detail.html", context)

def inventory_item_upc_delete_view(request, inventory_item_id, id):
    obj = get_object_or_404(InventoryItemUPC, inventory_item=inventory_item_id, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        "object": obj
    }
    return render(request, "inventory_item_upc/inventory_item_upc_delete.html", context)

#I need to fix the validation of the store name
def store_transfer_view(request):
    form = StoreTransferForm(request.POST or None)
    if form.is_valid():
        # I need to make a csv file upload then process it, folders won't work I need to create an app
        store_name = form.cleaned_data['store_name']
        csv_file = request.FILES.get('csvfile')
        StoreTransfer_start(store_name, csv_file)
    context = {
        'form': form
    }
    return render(request, "store_transfer/store_transfer_index.html", context)