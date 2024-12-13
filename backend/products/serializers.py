from rest_framework import serializers
from .models import Products, Variants



class VariantsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Variants
        fields = ["id", "name", "options","quantity"]

class ProductSerializer(serializers.ModelSerializer):
    variants = VariantsSerializer(many=True)

    class Meta:
        model = Products
        fields = [
            "id",
            "ProductName",
            "ProductCode",
            "ProductID",
            "ProductImage",
            "CreatedDate",
            "UpdatedDate",
            "CreatedUser",
            "TotalStock",
            "HSNCode",
            "Price",
            "variants",
        ]
        read_only_fields = ["id", "CreatedDate", "UpdatedDate"]

    def create(self, validated_data):
        variants_data = validated_data.pop("variants", [])
        total_qty = sum([data["quantity"] for data in variants_data])
        validated_data["TotalStock"] = total_qty
        product = Products.objects.create(**validated_data)
        for variant_data in variants_data:
            _= Variants.objects.create(product=product, **variant_data)
        return product