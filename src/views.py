from rest_framework import viewsets, filters

from src.models import Offer, Category
from src.serializers import OfferSerializer, CategorySerializer, OfferListSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name']


class OfferViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        'list': OfferListSerializer,
    }
    default_serializer_class = OfferSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        queryset = Offer.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset
