from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Menu_Item


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
    cuisine = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )
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