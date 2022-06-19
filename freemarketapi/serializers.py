from rest_framework import serializers

from freemarketapi.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'quantity', 'price', 'order')


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rating', 'product')


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ('id', 'images', 'product')


class OrderSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField(method_name='get_total_sum')

    def get_total_sum(self, order: Order) -> str:
        from decimal import Decimal
        summa: Decimal = Decimal(0.)
        for product in order.product_set:
            summa += Decimal(product.price)
        return str(summa)

    class Meta:
        model = Order
        fields = ('id', 'user', 'comment', 'total_sum')


class MarketUserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = MarketUser
        fields = ('id', 'user', 'phone')
