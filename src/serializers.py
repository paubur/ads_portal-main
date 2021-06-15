from rest_framework import serializers

from src.models import Category, Offer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class OfferListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('id', 'title', 'price', 'category')


class OfferSerializer(OfferListSerializer):
    class Meta(OfferListSerializer.Meta):
        fields = OfferListSerializer.Meta.fields + ('description', 'created_at')