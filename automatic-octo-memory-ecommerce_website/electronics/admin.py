from django.contrib import admin
from.models import Electronics

# Register your models here.
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'Price')

admin.site.register(Electronics, ElectronicsAdmin)
