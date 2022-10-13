from rest_framework import permissions,response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .models import Product
from . import serializers
from .permissions import IsAuthor


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.ProductDetailSerializer

    def get_permissions(self):
        if self.action in ('update','partial_update','destroy'):
            return [permissions.IsAuthenticated(),IsAuthor()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(owner =self.request.user)

