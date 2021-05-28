from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from product.serializers import ProductSerializer
from product.models import Product
from user.permissions import IsSuperUser, IsStaff
from user.serializers import UserSerializer


class ProductListCreateAPI(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & IsStaff | IsSuperUser]
    queryset = Product.objects.filter()

    def perform_create(self, serializer):
        created_by = UserSerializer(self.request.user).data
        serializer.save(created_by=created_by)


class ProductRetrieveUpdateAPI(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.filter()
    lookup_field = 'pk'

    def perform_update(self, serializer):
        updated_by = UserSerializer(self.request.user).data
        serializer.save(created_by=updated_by)
