from django.db import models
from django.urls import reverse
# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("storetransfer:store-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.store_name
# The distributor model
class Distributor(models.Model):
    distributor_name = models.CharField(max_length=100, unique=True)
    distributor_email = models.EmailField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("storetransfer:distributor-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.distributor_name

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("storetransfer:category-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.category_name

class Size(models.Model):
    size_name = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse("storetransfer:size-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.size_name

class Item(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item_sku = models.IntegerField()
    item_upc = models.IntegerField()
    item_distributor = models.ForeignKey(Distributor, on_delete=models.PROTECT)
    item_size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    item_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=100)
    item_case_cost = models.DecimalField(max_digits=13,decimal_places=2)
    item_split_bottle_cost = models.DecimalField(max_digits=13,decimal_places=2)
    item_retail_price = models.DecimalField(max_digits=13,decimal_places=2)
    item_MPQ = models.IntegerField()
    item_on_hand_count = models.IntegerField()
    item_error_value = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("storetransfer:item-detail", kwargs={"store_id": self.store.id, "id": self.id})

class InventoryItem(models.Model):
    inventory_item_sku = models.IntegerField()
    inventory_item_distributor = models.ForeignKey(Distributor, on_delete=models.PROTECT)
    inventory_item_size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    inventory_item_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    inventory_item_upc = models.IntegerField()
    inventory_item_name = models.CharField(max_length=100)
    inventory_item_case_cost = models.DecimalField(max_digits=13,decimal_places=2)
    inventory_item_split_bottle_cost = models.DecimalField(max_digits=13,decimal_places=2)
    inventory_item_MPQ = models.IntegerField()

    def get_absolute_url(self):
        return reverse("storetransfer:inventory-item-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.inventory_item_name