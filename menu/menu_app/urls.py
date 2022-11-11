from django.urls import path
from . import views

# urlpatterns = [
# path('menu/', views.get_menu),
# path('menu_cat/<int:year>/', views.menu_by_cat),
# path('menu_cui/<str:letter>/', views.menu_by_cuisine),

# ]

urlpatterns = [
    path('', views.get_menu, name='menu'),
    # path('Cuisine', views.menu_by_cuisine, name='cuisine'),
    path('<int:cuisine_pick>/', views.menu_by_cuisine),
    path('tesing_view', views.testing_view)
]