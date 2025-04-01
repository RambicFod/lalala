
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('', views.product_list, name='product_list'),
    path('primary', views.primary),
path('primary', views.primary, name='glava'),
]
