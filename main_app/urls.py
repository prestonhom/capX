from django.contrib.auth.models import User
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.OrderList.as_view(), name='order_index'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreate.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', views.OrderDelete.as_view(), name='order_delete'),
    path('accounts/signup', views.signup, name='signup'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('orders/<int:pk>/execute/', views.order_execute, name='order_execute'),

    
    # path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
]