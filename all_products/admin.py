from django.contrib import admin
from . import models

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    
class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Color, ColorAdmin)
admin.site.register(models.ReceivingTime)
admin.site.register(models.AllProduct)
admin.site.register(models.Review)
