from django.urls import path, include
from . import views

urlpatterns = [
    path('roles/', views.RoleList.as_view()),
    path('role-type/<int:pk>/', views.RoleDetail.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<str:username>/', views.UserDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:user_Id>/', views.OrderDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:product_Id>/', views.ReviewDetail.as_view()),
    path('images/', views.ImageList.as_view()),
    path('images/<int:product_Id>/', views.ImageDetail.as_view()),
    path('images-delete/<int:pk>/', views.ImageDelete.as_view()),
    path('sizes/', views.SizeList.as_view()),
    path('sizes/<int:pk>/', views.SizeDetail.as_view()),
    path('colors/', views.ColorList.as_view()),
    path('colors/<str:color>/', views.ColorDetail.as_view()),
    path('shopping-carts/', views.ShoppingCartList.as_view()),
    path('shopping-carts/<int:user_Id>/', views.ShoppingCartDetail.as_view()),
    path('shopping-carts-update/<int:pk>/', views.ShoppingCartUpdate.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]