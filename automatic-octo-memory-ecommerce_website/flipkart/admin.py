from django.contrib import admin

from .models import Shoes,  Electronics

# Register your models here.
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'Price')

admin.site.register(Electronics, ElectronicsAdmin)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock')


admin.site.register(Shoes,ShoesAdmin)
