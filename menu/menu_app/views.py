from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pprint import pprint
from .models import Menu_Item, Category, Cuisine
from django.forms.models import model_to_dict


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_menu(request):
    test = Menu_Item.objects.all()
    test_list = []
    for item in test:
        Category_model = Category.objects.get(id=item.category_id)
        Cuisine_model = Cuisine.objects.get(id=item.cuisine_id)
        test_list.append(
            {
            "Name" : item.title,
            "Description" : item.description,
            "Price" : item.price,
            "Spicy Level" : item.spice_level,
            "Category" : {"Name" : Category_model.title},
            "Cuisine" : {"Name" : Cuisine_model.title},
            }
        )
    # menu = list(Menu_Item.objects.values())
    return JsonResponse({'Menu Item' : test_list})

# def menu_by_cat(request, category_pick):
#     menu_by_category= list(MenuItem.objects.filter( category = category_pick).values())
#     pprint(menu_by_category)
#     return JsonResponse({'Menu Item' : menu_by_category})

def menu_by_cuisine(request, cuisine_pick):
    menu_by_area= (MenuItem.objects.filter( cuisine = cuisine_pick).all())
    test_list = []
    for item in test:
        Category_model = Category.objects.get(id=item.category_id)
        Cuisine_model = Cuisine.objects.get(id=item.cuisine_id)
        test_list.append(
            {
            "Name" : item.title,
            "Description" : item.description,
            "Price" : item.price,
            "Spicy Level" : item.spice_level,
            "Category" : {"Name" : Category_model.title},
            "Cuisine" : {"Name" : Cuisine_model.title},
            }
        )
    # menu = list(Menu_Item.objects.values())
    return JsonResponse({'Menu Item' : test_list})