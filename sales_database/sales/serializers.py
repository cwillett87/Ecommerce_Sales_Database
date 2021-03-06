from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'type']


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'role', 'username', 'password', 'email', 'address', 'phone', 'first_name', 'last_name']


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ['id', 'role', 'username', 'password', 'email', 'address', 'phone', 'first_name', 'last_name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'creator_Id', 'name', 'description', 'price', 'ave_rating', 'quantity', 'main_image']


class PostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'creator_Id', 'name', 'description', 'price', 'ave_rating', 'quantity', 'main_image']


class ShoppingCartSerializer(serializers.ModelSerializer):
    product_Id = ProductSerializer(read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user_Id', 'product_Id', 'color_Id', 'size_Id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user_Id = UserSerializer(read_only=True)
    shopping_carts = ShoppingCartSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ['id', 'shopping_carts', 'user_Id', 'tracking_number', 'total', 'checked_Out']


class PostOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'shopping_carts', 'user_Id', 'tracking_number', 'total', 'checked_Out']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product_Id', 'review', 'rating']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'product_Id', 'path']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['size']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color']


class PostShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'user_Id', 'product_Id', 'color_Id', 'size_Id', 'quantity']
