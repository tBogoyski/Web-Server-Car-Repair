"""CarShopUNI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import cars.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cars.views.IndexView.as_view(), name='index'),
    path('list/', cars.views.CarListView.as_view(), name='car_list'),
    path('add-car/', cars.views.CarCreateView.as_view(), name='add_car'),
    path('car/<int:pk>/', cars.views.CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/delete/', cars.views.CarDeleteView.as_view(), name='car_delete'),
    path('car/<int:pk>/update/', cars.views.CarUpdateView.as_view(), name='car_update'),
]
