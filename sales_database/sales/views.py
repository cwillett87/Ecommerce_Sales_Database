from .models import Role, User, Product, Order, Review, Image, Size, Color, ShoppingCart
from .serializers import RoleSerializer, OrderSerializer, UserSerializer, ProductSerializer, ReviewSerializer, ImageSerializer, SizeSerializer, ColorSerializer, ShoppingCartSerializer, PostShoppingCartSerializer
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

    def get_object(self, pk):
        try:
            return Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        role = self.get_object(pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    def put(self, request, pk):
        role = self.get_object(pk)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        role = self.get_object(pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):

    def get(self, request):
        user = User.objects.all()
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
            return User.objects.get(username=username)
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
            return Order.objects.get(user_Id=user_Id)
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
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product= self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
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

    def get_object(self, product_Id):
        try:
            return Image.objects.filter(product_Id=product_Id)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, product_Id):
        image = self.get_object(product_Id)
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)


class ImageDelete(APIView):

    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def delete(self, request, pk):
        image = self.get_object(pk)
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

    def get_object(self, pk):
        try:
            return Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        size = self.get_object(pk)
        serializer = SizeSerializer(size)
        return Response(serializer.data)

    def put(self, request, pk):
        size = self.get_object(pk)
        serializer = SizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        size = self.get_object(pk)
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
            return Color.objects.get(color=color)
        except Color.DoesNotExist:
            raise Http404

    def get(self, request, color):
        color = self.get_object(color)
        serializer = ColorSerializer(color)
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
        serializer = PostShoppingCartSerializer(data=request.data)
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


class ShoppingCartUpdate(APIView):

    def get_object(self, pk):
        try:
            return ShoppingCart.objects.get(pk=pk)
        except ShoppingCart.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        shoppingCart = self.get_object(pk)
        serializer = ShoppingCartSerializer(shoppingCart)
        return Response(serializer.data)

    def put(self, request, pk):
        shoppingCart = self.get_object(pk)
        serializer = ShoppingCartSerializer(shoppingCart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        shoppingCart = self.get_object(pk)
        shoppingCart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
