"""ecom_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from ecom_project.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', health_check),
    path('api/v1/users', include('user.urls', namespace='user-api')),
    path('api/v1/shops', include('shop.urls', namespace='shop-api')),
    path('api/v1/wallet', include('wallet.urls', namespace='wallet-api')),
    path('api/v1/products', include('product.urls', namespace='product-api')),
]
