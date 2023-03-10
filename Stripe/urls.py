"""Stripe URL Configuration

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
from payments.views import buy_item, show_item, success, cancel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('item/<int:item_id>/', show_item, name='show_item'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel')
]
