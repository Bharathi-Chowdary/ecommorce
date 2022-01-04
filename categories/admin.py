from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    
#this is written coz whenever we add the category name in webserver category url will get auto-filled
    prepopulated_fields = {'url': ('name',)}
    list_display = ('name', 'url')
    
admin.site.register(Category, CategoryAdmin)


