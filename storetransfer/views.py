from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
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
    object_list = Item.objects.filter(store=id).order_by('item_error_value')
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

def inventory_item_create_view(request, distributor_id):
    form = InventoryItemForm(request.POST or None, initial={'inventory_item_distributor':distributor_id})
    if form.is_valid():
        form.save()
        return redirect('storetransfer:inventory-item-list', distributor_id)
    context = {
        'form': form
    }
    return render(request, "inventory_item/inventory_item_create.html", context)

def inventory_item_update_view(request, id):
    obj = get_object_or_404(InventoryItem, id=id)
    form = InventoryItemForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        distributor_id = obj.inventory_item_distributor_id
        return redirect('storetransfer:inventory-item-list', distributor_id)
    context = {
        'form': form
    }
    return render(request, "inventory_item/inventory_item_create.html", context)

def inventory_item_list_view(request, distributor_id):
    if distributor_id == 0:
        queryset = InventoryItem.objects.all()
    else:
        queryset = InventoryItem.objects.filter(inventory_item_distributor=distributor_id)
    count = len(queryset)
    context = {
        "object_list": queryset,
        "count": count,
        "distributor_id": distributor_id
    }
    return render(request, "inventory_item/inventory_item_list.html", context)

def inventory_item_distributor_list_view(request):
    queryset = Distributor.objects.all()
    count = len(queryset)
    if request.method == "POST":
        distributor_id = request.POST['dropdown']
        return redirect('storetransfer:inventory-item-list', distributor_id)
    context = {
        "object_list": queryset,
        "count": count
    }
    return render(request, "inventory_item/inventory_item_distributor_list.html", context)

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
        distributor_id = obj.inventory_item_distributor_id
        obj.delete()
        return redirect('storetransfer:inventory-item-list', distributor_id)
    context = {
        "object": obj
    }
    return render(request, "inventory_item/inventory_item_delete.html", context)

def item_create_view(request, store_id):
    form = ItemForm(request.POST or None, initial={'store':store_id})
    if form.is_valid():
        form.save()
        return redirect('storetransfer:store-detail', store_id)
    context = {
        'form': form
    }
    return render(request, "item/item_create.html", context)

def item_update_view(request, store_id, id):
    obj = get_object_or_404(Item, store=store_id, id=id)
    form = ItemForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('storetransfer:store-detail', store_id)
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
        return redirect('storetransfer:store-detail', store_id)
    context = {
        "object": obj
    }
    return render(request, "item/item_delete.html", context)

#I need to fix the validation of the store name
def store_transfer_view(request):
    form = StoreTransferForm(request.POST or None)
    if form.is_valid():
        # I need to make a csv file upload then process it, folders won't work I need to create an app
        store_name = form.cleaned_data['store_name']
        csv_file = request.FILES['csvfile']
        try:
            store_id = StoreTransfer_start(store_name, csv_file)
            return redirect('storetransfer:store-detail', store_id)
        except Exception as e:
           messages.info(request, e.args)
    context = {
        'form': form
    }
    return render(request, "store_transfer/store_transfer_index.html", context)

def create_store_store_creation_view(request):
    form = StoreForm(request.POST or None)
    if form.is_valid():
        new_store = form.save()
        store_id = new_store.pk
        return redirect('storetransfer:create-store-distributor-selection', store_id)
    context = {
        'form': form
    }
    return render(request, "create_store/create_store_store_creation.html", context)

def create_store_distributor_selection_view(request, store_id):
    queryset = Distributor.objects.all()
    count = len(queryset)
    if request.method == "POST":
        distributor_id = request.POST['dropdown']
        return redirect('storetransfer:create-store-add-items', store_id, distributor_id)
    context = {
        "object_list": queryset,
        "count": count
    }
    return render(request, "create_store/create_store_distributor_list.html", context)

def create_store_add_items_view(request, store_id, distributor_id):
    distributor_name = ''
    if distributor_id == 0:
        queryset = InventoryItem.objects.all()
        distributor_name = 'All Items'
    else:
        queryset = InventoryItem.objects.filter(inventory_item_distributor=distributor_id)
        distributor = get_object_or_404(Distributor, id=distributor_id)
        distributor_name = distributor.distributor_name
    count = len(queryset)
    context = {
        "object_list": queryset,
        "count": count,
        "distributor_id": distributor_id,
        "distributor_name": distributor_name
    }
    return render(request, "create_store/create_store_distributor_inventory_items.html", context)