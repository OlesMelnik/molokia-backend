from rest_framework import serializers
from products.models import Product, State, StateProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StateProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = StateProduct
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = State
        fields = '__all__'