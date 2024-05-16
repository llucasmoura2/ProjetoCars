from django.contrib import admin
from cars.models import Car, Brand


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand') # o campo de busca mostra só os mmodelos

    

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
