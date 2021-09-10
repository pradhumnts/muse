from django.contrib import admin
from .models import Category, MenuItem
from ordered_model.admin import OrderedModelAdmin

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    # ...
    list_display = ('title', 'description', 'price', 'active')

class CategoryAdmin(OrderedModelAdmin):
    # ...
    list_display = ('category', 'active', 'move_up_down_links')

admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)