from django_filters import FilterSet, filters
from django_filters.widgets import CSVWidget

from ..models.store import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ('min_price', 'max_price', 'category')

    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = filters.BaseInFilter(field_name='category__name', lookup_expr='in', widget=CSVWidget)
    search = filters.CharFilter(field_name='name', lookup_expr='icontains')