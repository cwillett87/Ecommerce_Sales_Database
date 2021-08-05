from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    type = models.CharField(primary_key=True, max_length=50)


class User(AbstractUser):
    role = models.ForeignKey('sales.Role', null=True, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField(blank=True, null=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'role', 'address', 'phone']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Product(models.Model):
    creator_Id = models.ForeignKey('sales.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=60, decimal_places=2)
    ave_rating = models.DecimalField(default=0, max_digits=60, decimal_places=2)
    quantity = models.IntegerField()
    main_image = models.CharField(max_length=50)


class Review(models.Model):
    product_Id = models.ForeignKey('sales.Product', blank=True, null=True, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)
    rating = models.IntegerField()


class Image(models.Model):
    product_Id = models.ForeignKey('sales.Product', blank=True, null=True, on_delete=models.CASCADE)
    path = models.CharField(max_length=50)


class Size(models.Model):
    size = models.CharField(primary_key=True, max_length=50)


class Color(models.Model):
    color = models.CharField(primary_key=True, max_length=50)


class ShoppingCart(models.Model):
    user_Id = models.ForeignKey('sales.User', null=False, on_delete=models.CASCADE)
    product_Id = models.ForeignKey('sales.Product', null=False, on_delete=models.CASCADE)
    color_Id = models.ForeignKey('sales.Color', null=False, on_delete=models.CASCADE)
    size_Id = models.ForeignKey('sales.Size', null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    shopping_carts = models.ManyToManyField(ShoppingCart, null=True)
    user_Id = models.ForeignKey('sales.User', null=False, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=50)
    total = models.DecimalField(default=0, max_digits=60, decimal_places=2)
    checked_Out = models.BooleanField(default=False)
