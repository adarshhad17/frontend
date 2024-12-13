from django.db import models
from versatileimagefield.fields import VersatileImageField
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    ProductID = models.BigIntegerField(unique=True)    
    ProductCode = models.CharField(max_length=255, unique=True)
    ProductName = models.CharField(max_length=255)    
    ProductImage = VersatileImageField(upload_to="uploads/", blank=True, null=True)    
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(blank=True, null=True)
    CreatedUser = models.ForeignKey("auth.User", related_name="user%(class)s_objects", on_delete=models.CASCADE)    
    IsFavourite = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)    
    HSNCode = models.CharField(max_length=255, blank=True, null=True)    
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)
    Price = models.FloatField(default=0.00,blank=True,null=True)
    class Meta:
        db_table = "products_product"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        unique_together = (("ProductCode", "ProductID"),)
        ordering = ("-CreatedDate", "ProductID")


class Variants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey("Products", related_name="variants", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    options =  models.JSONField(blank=True, default=list)
    quantity = models.IntegerField(default=0.0,blank=True,null=True)
    class Meta:
        db_table = "products_variants"
        verbose_name = _("variant")
        verbose_name_plural = _("variants")


class StockManagement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    change = models.DecimalField(max_digits=20, decimal_places=8)
    reason = models.CharField(max_length=255, choices=[("PURCHASE", "Purchase"), ("SALE", "Sale")])
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "products_stock_management"
        verbose_name = _("stock_management")
        verbose_name_plural = _("stock_management")