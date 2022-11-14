
# from django.contrib import admin
# from django.urls import path, include
# import menu_app
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('menu_app/', include('menu_app.urls')),
#     # path('', include(menu_app.urls))
# ]


from django.urls import include, path
from rest_framework import routers
from menu_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'menu_items', views.Menu_ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]