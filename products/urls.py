
from django import views
from django.urls import path
from .views import product_list, product_detail, create_product, edit_product, delete_product
from .views import signup

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', create_product, name='create_product'),
    path('signup/', signup, name='signup'),
    path('<int:id>/', product_detail, name='product_detail'),
    path('<int:pk>/edit/', edit_product, name='edit_product'),
    path('<int:pk>/delete/', delete_product, name='delete_product'),
]