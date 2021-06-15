import factory
from factory import Faker

from src.models import Category, Offer


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = Faker('word')


class OfferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Offer

    title = Faker('word')
    description = Faker('sentence', nb_words=4)
    price = Faker('pydecimal', positive=True)
    category = factory.SubFactory(CategoryFactory)


