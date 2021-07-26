from django.contrib import admin
from .models import Role, User, Order, Product, Review, Image, Size, Color, ShoppingCart
# Register your models here.

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ShoppingCart)
