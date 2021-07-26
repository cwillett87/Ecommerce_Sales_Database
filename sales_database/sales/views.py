from .models import Role, User, Product, Order, Review, Image, Size, Color, ShoppingCart
from .serializers import RoleSerializer, OrderSerializer, UserSerializer, ProductSerializer, ReviewSerializer, ImageSerializer, SizeSerializer, ColorSerializer, ShoppingCartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.


class RoleList(APIView):

    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetail(APIView):

    def get_object(self, role):
        try:
            return Role.objects.filter(role=role)
        except Role.DoesNotExist:
            raise Http404

    def get(self, request, role):
        role = self.get_object(role)
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data)

    def put(self, request, role):
        role = self.get_object(role)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, role):
        role = self.get_object(role)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):

    def get(self, request):
        user = Role.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, username):
        try:
            return User.objects.filter(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def put(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = self.get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):

    def get_object(self, user_Id):
        try:
            return Order.objects.filter(user_Id=user_Id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, user_Id):
        order = self.get_object(user_Id)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def put(self, request, user_Id):
        order= self.get_object(user_Id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_Id):
        order = self.get_object(user_Id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(APIView):

    def get(self, request):
        product = Product.objects.all()
        serializer = OrderSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get_object(self, id):
        try:
            return Product.objects.filter(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        product= self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewList(APIView):

    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):

    def get_object(self, product_Id):
        try:
            return Review.objects.filter(product_Id=product_Id)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, product_Id):
        review = self.get_object(product_Id)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def put(self, request, product_Id):
        review = self.get_object(product_Id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_Id):
        review = self.get_object(product_Id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageList(APIView):

    def get(self, request):
        image = Image.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(APIView):

    def get_object(self, name):
        try:
            return Image.objects.filter(name=name)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, name):
        image = self.get_object(name)
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)

    def put(self, request, name):
        image = self.get_object(name)
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        image = self.get_object(name)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SizeList(APIView):

    def get(self, request):
        size = Size.objects.all()
        serializer = SizeSerializer(size, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SizeDetail(APIView):

    def get_object(self, size):
        try:
            return Size.objects.filter(size=size)
        except Size.DoesNotExist:
            raise Http404

    def get(self, request, size):
        size = self.get_object(size)
        serializer = SizeSerializer(size, many=True)
        return Response(serializer.data)

    def put(self, request, size):
        size = self.get_object(size)
        serializer = SizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, size):
        size = self.get_object(size)
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ColorList(APIView):

    def get(self, request):
        color = Color.objects.all()
        serializer = ColorSerializer(color, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorDetail(APIView):

    def get_object(self, color):
        try:
            return Color.objects.filter(color=color)
        except Color.DoesNotExist:
            raise Http404

    def get(self, request, color):
        color = self.get_object(color)
        serializer = ColorSerializer(color, many=True)
        return Response(serializer.data)

    def put(self, request, color):
        color = self.get_object(color)
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, color):
        color = self.get_object(color)
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShoppingCartList(APIView):

    def get(self, request):
        shoppingCart = ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(shoppingCart, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShoppingCartDetail(APIView):

    def get_object(self, user_Id):
        try:
            return ShoppingCart.objects.filter(user_Id=user_Id)
        except ShoppingCart.DoesNotExist:
            raise Http404

    def get(self, request, user_Id):
        shoppingCart = self.get_object(user_Id)
        serializer = ShoppingCartSerializer(shoppingCart, many=True)
        return Response(serializer.data)

    def put(self, request, user_Id):
        shoppingCart = self.get_object(user_Id)
        serializer = ShoppingCartSerializer(shoppingCart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_Id):
        shoppingCart = self.get_object(user_Id)
        shoppingCart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
