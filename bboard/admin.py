from django.contrib import admin
from .models import Bboard


# Register your models here.

class BboardAdmin(admin.ModelAdmin):
    list_display = (
        'rent', 'category', 'area_value', 'area_unit', 'rooms', 'floor', 'price', 'period', 'internet', 'parking')


admin.site.register(Bboard, BboardAdmin)
