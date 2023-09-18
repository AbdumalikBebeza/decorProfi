from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    catalog_name = serializers.SerializerMethodField()
    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "name articul model catalog brand description color image1 image2 image3" \
                 " image4 information price catalog_name brand_name".split()

    def get_catalog_name(self, product):
        return product.catalog_name

    def get_brand_name(self, product):
        return product.brand_name
