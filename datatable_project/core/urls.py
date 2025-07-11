from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos_list, name='productos_list'),
    path('productos/ajax/', views.productos_ajax, name='productos_ajax'),
]
