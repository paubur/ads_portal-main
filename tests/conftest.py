import pytest

from tests.factories.test_factories import CategoryFactory, OfferFactory


@pytest.fixture
def basic_category():
    obj = CategoryFactory()
    yield obj
    obj.delete()


@pytest.fixture
def basic_offer():
    obj = OfferFactory()
    yield obj
    obj.delete()
