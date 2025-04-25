from rest_framework import viewsets, serializers


from ..models.store import Category
from ..permissions import SafeMethods

class CategoryViewSet(viewsets.ModelViewSet):
    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = '__all__'

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [SafeMethods]