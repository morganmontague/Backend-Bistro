from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Menu_Item, Category, Cuisine

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    menu_items_by_categories = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Category
        fields = ['title', 'menu_items_by_categories']

class CuisineSerializer(serializers.HyperlinkedModelSerializer):
    menu_item_by_cuisines = serializers.StringRelatedField(many=True)
    class Meta:
        model = Cuisine
        fields = ['title', 'menu_item_by_cuisines']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class Menu_ItemSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField(many=False)
    cuisine = serializers.StringRelatedField(many=False)
    ingredients = serializers.StringRelatedField(many=True)
    class Meta:
        model = Menu_Item
        fields = [
            'title',
            'description',
            'price',
            'spice_level',
            'category',
            'cuisine',
            'ingredients'
        ]