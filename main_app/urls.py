from django.contrib.auth.models import User
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.OrderList.as_view(), name='order_index'),
    #path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('accounts/signup', views.signup, name='signup'),
    
    # path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
]