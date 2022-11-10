from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pprint import pprint
# from .models import Menu_Item


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_menu(request):
    menu = list(MenuItem.objects.values())
    pprint(menu)
    return JsonResponse({'Menu Item' : Menu})

# def menu_by_cat(request, category_pick):
#     menu_by_category= list(MenuItem.objects.filter( category = category_pick).values())
#     pprint(menu_by_category)
#     return JsonResponse({'Menu Item' : menu_by_category})

# def menu_by_cuisine(request, cuisine_pick):
#     menu_by_area= list(MenuItem.objects.filter( cuisine = cuisine_pick).values())
#     pprint(menu_by_area)
#     return JsonResponse({'Menu Item' : menu_by_area})