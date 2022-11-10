from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pprint import pprint
from .models import Menu_Item, Category, Cuisine
from django.forms.models import model_to_dict


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_menu(request):
    test = Menu_Item.objects.all()
    list_of_menu = []
    for item in test:
        Category_model = Category.objects.get(id=item.category_id)
        Cuisine_model = Cuisine.objects.get(id=item.cuisine_id)
        list_of_menu.append(
            {
            "title" : item.title,
            "description" : item.description,
            "price" : item.price,
            "spicy Level" : item.spice_level,
            "category" : {"title" : Category_model.title},
            "cuisine" : {"title" : Cuisine_model.title},
            }
        )
    # menu = list(Menu_Item.objects.values())
    return JsonResponse(list_of_menu, safe=False)

# def menu_by_cat(request, category_pick):
#     menu_by_category= list(MenuItem.objects.filter( category = category_pick).values())
#     pprint(menu_by_category)
#     return JsonResponse({'Menu Item' : menu_by_category})

def menu_by_cuisine(request, cuisine_pick):
    menu_by_area= (Menu_Item.objects.filter( cuisine = cuisine_pick).all())
    list_of_menu = []
    for item in menu_by_area:
        Category_model = Category.objects.get(id=item.category_id)
        Cuisine_model = Cuisine.objects.get(id=item.cuisine_id)
        list_of_menu.append(
            {
            "name" : item.title,
            "description" : item.description,
            "price" : item.price,
            "spicy Level" : item.spice_level,
            "category" : {"Name" : Category_model.title},
            "cuisine" : {"Name" : Cuisine_model.title},
            }
        )
    # menu = list(Menu_Item.objects.values())
    return JsonResponse(list_of_menu, safe = False)