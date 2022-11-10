from django.contrib import admin

from .models import Menu_Item
from .models import Category
from .models import Cuisine

admin.site.register(Menu_Item)
admin.site.register(Category)
admin.site.register(Cuisine)