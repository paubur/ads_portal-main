from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from src.views import OfferViewSet, CategoryViewSet

offer_list = OfferViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
offer_detail = OfferViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
    'post': 'create'
})

urlpatterns = format_suffix_patterns([
    path('offers/', offer_list, name='offer-list'),
    path('offers/<int:pk>/', offer_detail, name='offer-detail'),
    path('category/', category_list, name='category-list'),
    path('category/<int:pk>/', category_detail, name='category-detail')
])
