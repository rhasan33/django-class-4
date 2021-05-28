from django.urls import path

from product.views import ProductListCreateAPI, ProductRetrieveUpdateAPI

app_name = 'product'

urlpatterns = [
    path('', ProductListCreateAPI.as_view(), name='product-create-list-api'),
    path('/<int:pk>', ProductRetrieveUpdateAPI.as_view(), name='product-get-list-api'),
]
