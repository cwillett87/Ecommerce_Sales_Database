from django.db import models


class Role(models.Model):
    type = models.CharField(max_length=50)


class User(models.Model):
    role = models.ForeignKey('sales.Role', null=False, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Order(models.Model):
    user_Id = models.ForeignKey('sales.User', null=False, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=50)
    total = models.IntegerField()
    checked_Out = False


class Product(models.Model):
    creator_Id = models.ForeignKey('sales.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    ave_rating = models.IntegerField()
    quantity = models.IntegerField()


class Review(models.Model):
    product_Id = models.ForeignKey('sales.Product', blank=True, null=True, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)
    rating = models.IntegerField()


class Image(models.Model):
    product_Id = models.ForeignKey('sales.Product', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Size(models.Model):
    size = models.CharField(max_length=50)


class Color(models.Model):
    color = models.CharField(max_length=50)


class ShoppingCart(models.Model):
    user_Id = models.ForeignKey('sales.User', null=False, on_delete=models.CASCADE)
    product_Id = models.ForeignKey('sales.Product', null=False, on_delete=models.CASCADE)
    color_Id = models.ForeignKey('sales.Color', null=False, on_delete=models.CASCADE)
    size_Id = models.ForeignKey('sales.Size', null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField()
