from rest_framework import serializers
from products.models import Product, Designer


class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    designer = serializers.CharField(source="designer.name", read_only=True)
    designer_id = serializers.PrimaryKeyRelatedField(
        queryset=Designer.objects.all(), source="designer", write_only=True
    )

    class Meta:
        model = Product
        fields = "__all__"
