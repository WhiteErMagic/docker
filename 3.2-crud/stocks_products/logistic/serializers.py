from .models import Product, Stock, StockProduct
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ("address", "positions")

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # # создаем склад по его параметрам
        stock = Stock.objects.get_or_create(validated_data)[0]
        for position in positions:

            StockProduct.objects.update_or_create(
                stock_id=stock.id, product_id=position['product'].id,
                defaults={'quantity': position['quantity'], 'price': position['price']}
            )

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = Stock.objects.get_or_create(validated_data)[0]

        for position in positions:
            StockProduct.objects.update_or_create(
                stock_id=stock.id, product_id=position['product'].id,
                defaults={'quantity': position['quantity'], 'price': position['price']}
            )
        return stock
