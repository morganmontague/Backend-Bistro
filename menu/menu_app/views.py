# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from pprint import pprint
# from .models import Menu_Item, Category, Cuisine, Ingredients
# from django.forms.models import model_to_dict

# def get_menu(request):
#     test = Menu_Item.objects.all()
#     list_of_menu = []
    
#     def remove_stuff(x):
#         new_x = x.replace("[", '')
#         new_x = new_x.replace("]", '')
#         new_x = new_x.replace("(", '')
#         new_x = new_x.replace(")", '')
#         new_x = new_x.replace(",", '')
#         new_x = new_x.replace("'", '')
#         return new_x

#     for item in test:
#         Category_model = Category.objects.get(id=item.category_id)
#         Cuisine_model = Cuisine.objects.get(id=item.cuisine_id)
#         # Ingredients_model = Ingredients.objects.get(id=item.ingredients_id)
#         list_of_menu.append(
#             {
#             "title" : item.title,
#             "description" : item.description,
#             "price" : item.price,
#             "spicy Level" : item.spice_level,
#             "category" : {"title" : Category_model.title},
#             "cuisine" : {"title" : Cuisine_model.title},
#             "ingredients" : remove_stuff(''.join(str(list(item.ingredients.values_list('title'))))),
#             }
#         )
#     # menu = list(Menu_Item.objects.values())
#     return JsonResponse(list_of_menu, safe=False)

# # def menu_by_cat(request, category_pick):
# #     menu_by_category= list(MenuItem.objects.filter( category = category_pick).values())
# #     pprint(menu_by_category)
# #     return JsonResponse({'Menu Item' : menu_by_category})

# def menu_by_cuisine(request, cuisine_pick):
#     menu_by_area = (Menu_Item.objects.filter( cuisine = cuisine_pick).all())
#     list_of_menu = []
#     for item in menu_by_area:
#         Category_model = Category.objects.get(id=item.category_id)
#         Cuisine_model = Cuisine.objects.get(id=item.cuisine_id)
#         list_of_menu.append(
#             {
#             "title" : item.title,
#             "description" : item.description,
#             "price" : item.price,
#             "spicy Level" : item.spice_level,
#             "category" : {"title" : Category_model.title},
#             "cuisine" : {"title" : Cuisine_model.title},
#             "ingredients" : list(item.ingredients.values('title')),
#             }
#         )
#     # menu = list(Menu_Item.objects.values())
#     return JsonResponse(list_of_menu, safe = False)

# def testing_view(request):
#     test = Menu_Item.objects.all()
#     list_of_menu = []
    
#     def remove_stuff(x):
#         new_x = x.replace("[", '')
#         new_x = new_x.replace("]", '')
#         new_x = new_x.replace("(", '')
#         new_x = new_x.replace(")", '')
#         new_x = new_x.replace(",", '')
#         new_x = new_x.replace("'", '')
#         return new_x

#     for item in test:
#         Category_model = Category.objects.get(id=item.category_id)
#         Cuisine_model = Cuisine.objects.get(id=item.cuisine_id)
#         # Ingredients_model = Ingredients.objects.get(id=item.ingredients_id)
#         list_of_menu.append(
#             {
#             "title" : item.title,
#             "description" : item.description,
#             "price" : item.price,
#             "spicy Level" : item.spice_level,
#             "category" : {"title" : Category_model.title},
#             "cuisine" : {"title" : Cuisine_model.title},
#             "ingredients" : list(item.ingredients.values('title')),
#             "test_join" : ', '.join([str(x) for x in item.ingredients.values('title')]),
#             "join_test_two" : ''.join(str(list(item.ingredients.values('title')))),
#             "join_test_three" : ''.join(str(list(item.ingredients.values_list('title')))),
#             "join_test_four" : remove_stuff(''.join(str(list(item.ingredients.values_list('title'))))),
#             }
#         )
#     # menu = list(Menu_Item.objects.values())
#     return JsonResponse(list_of_menu, safe=False)

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, Menu_ItemSerializer, CategorySerializer, CuisineSerializer
from pprint import pprint
from .models import Menu_Item, Category, Cuisine, Ingredients
from django.forms.models import model_to_dict
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Menu Items to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CuisineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Menu Items to be viewed or edited.
    """
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

class Menu_ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Menu Items to be viewed or edited.
    """
    queryset = Menu_Item.objects.all()
    serializer_class = Menu_ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CuisineAPIView(APIView):
    def get_object(self, pk):
        try:
            return Menu_Item.get(pk = pk)
        except Menu_Item.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = Menu_ItemSerializer(data)

        else:
            data = Menu_Item.objects.all()
            serializer = Menu_ItemSerializer(data, many=True)

            return Response(serializer.data)

    # Create
    def post(self, request, format=None):
        data ={
            'title': request.POST.get('title', None),
            'description':request.POST.get('description', None),
            'price': request.POST.get('price', None),
            'spice_level': request.POST.get('spice_level', None),
            'category' : Category.id,
            'cuisine': Cuisine.id,
            'ingredients': request.POST.get('ingredients', None)
        }
        serializer = Menu_ItemSerializer(data=data)

        # Checl of True
        serializer.is_valid(raise_exception=True)

        # Save the data
        serializer.save()

        response = Response()

        response.data = {
            "message": 'Success',
            "data": serializer.data
        }
        return response

        

