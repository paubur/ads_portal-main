import pytest

from src.models import Category, Offer
from src.serializers import CategorySerializer, OfferSerializer


'''offer serializer'''
@pytest.mark.django_db
def test_offer_serializer(basic_offer):
    data = {'id': basic_offer.id,
            'title': basic_offer.title,
            'description': basic_offer.description,
            'price': round(basic_offer.price, 2),
            'created_at': basic_offer.created_at,
            'category': basic_offer.category.id,
            }
    serializer = OfferSerializer(data=data)
    assert serializer.is_valid() == True
    serializer.save()
    assert Offer.objects.all().count() == 2


@pytest.mark.django_db
def test_offer_serializer_wo_id(basic_offer):
    data = {'title': basic_offer.title,
            'description': basic_offer.description,
            'price': round(basic_offer.price, 2),
            'created_at': basic_offer.created_at,
            'category': basic_offer.category.id,
            }
    serializer = OfferSerializer(data=data)
    assert serializer.is_valid() == True
    serializer.save()
    assert Offer.objects.all().count() == 2


@pytest.mark.django_db
def test_offer_serializer_invalid_title(basic_offer):
    data = {'id': basic_offer.id,
            'description': basic_offer.description,
            'price': round(basic_offer.price, 2),
            'created_at': basic_offer.created_at,
            'category': basic_offer.category.id,
            }
    serializer = OfferSerializer(data=data)
    assert serializer.is_valid() == False


@pytest.mark.django_db
def test_offer_serializer_invalid_price(basic_offer):
    data = {'id': basic_offer.id,
            'title': basic_offer.title,
            'description': basic_offer.description,
            'price': basic_offer.price,
            'created_at': basic_offer.created_at,
            'category': basic_offer.category.id,
            }
    serializer = OfferSerializer(data=data)
    assert serializer.is_valid() == False


'''category serializer'''
@pytest.mark.django_db
def test_category_serializer():
    data = {'id': 1, 'name': 'name'}
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid() == True
    serializer.save()
    assert Category.objects.all().count() == 1


@pytest.mark.django_db
def test_category_serializer_invalid_name():
    data = {'id': 1}
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid() == False


@pytest.mark.django_db
def test_category_serializer_wo_id():
    data = {'name': 'name'}
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid() == True

