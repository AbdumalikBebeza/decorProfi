from django.contrib import admin
from .models import Product, Brand, Catalog, SubCatalog
# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Catalog)
admin.site.register(SubCatalog)