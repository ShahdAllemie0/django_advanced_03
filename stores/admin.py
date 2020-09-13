from django.contrib import admin
from .models import Store

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    fields=['name','description',]
    search_fields=['name','description']

admin.site.register(Store,StoreAdmin)
