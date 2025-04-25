from rest_framework import viewsets, serializers

from ..models.store import Product
from ..permissions import SafeMethods
from ..filters.product import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = '__all__'

    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    permission_classes = [SafeMethods]
    search_fields = ['search']
