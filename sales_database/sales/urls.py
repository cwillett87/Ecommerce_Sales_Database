from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.RoleList.as_view()),
    path('roles/<str:role>/', views.RoleDetail.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<str:username>/', views.UserDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:user_Id>/', views.OrderDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductDetail.as_view()),
    path('reviews/', views.RoleList.as_view()),
    path('reviews/<int:product_Id>/', views.ReviewDetail.as_view()),
    path('images/', views.ImageList.as_view()),
    path('images/<str:name>/', views.ImageDetail.as_view()),
    path('sizes/', views.SizeList.as_view()),
    path('sizes/<str:size>/',views.SizeDetail.as_view()),
    path('colors/', views.ColorList.as_view()),
    path('colors/<str:color>/', views.ColorDetail.as_view()),
    path('shoppingcarts/', views.ShoppingCartList.as_view()),
    path('shoppingcarts/<int:user_Id>/', views.ShoppingCartDetail.as_view()),
]