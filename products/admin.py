from django.contrib import admin
from .models import Product, Offer


# naming convention prefix with app name and add suffix as Admin
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name' , 'price' , 'stock')

admin.site.register(Offer,OfferAdmin)
admin.site.register(Product,ProductAdmin)