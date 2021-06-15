import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from src.models import Offer, Category
from tests.factories.test_factories import CategoryFactory, OfferFactory


'''offer model'''
@pytest.mark.django_db
def test_offer_create(basic_offer):
    assert len(Offer.objects.all()) == 1


@pytest.mark.django_db
def test_offer_isinstance(basic_offer):
    assert isinstance(basic_offer, Offer)


@pytest.mark.django_db
def test_offer_create_negative_price():
    with pytest.raises(ValidationError):
        obj = OfferFactory(price=-3)
        obj.full_clean()


@pytest.mark.django_db
def test_create_offer_wo_category():
    with pytest.raises(IntegrityError):
        OfferFactory(category=None)


@pytest.mark.django_db
def test_create_offer_wo_title():
    with pytest.raises(ValidationError):
        obj = OfferFactory(title='')
        obj.full_clean()


'''category model'''
@pytest.mark.django_db
def test_category_create(basic_category):
    assert len(Category.objects.all()) == 1


@pytest.mark.django_db
def test_category_isinstance(basic_category):
    assert isinstance(basic_category, Category)


@pytest.mark.django_db
def test_create_category_wo_name():
    with pytest.raises(ValidationError):
        obj = CategoryFactory(name='')
        obj.full_clean()
