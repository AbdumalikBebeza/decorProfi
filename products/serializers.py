from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    catalog_name = serializers.SerializerMethodField()
    brand_name = serializers.SerializerMethodField()
    sub_catalog_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "id name articul model catalog brand sub_catalog description color image1 image2 image3" \
                 " image4 information price catalog_name brand_name sub_catalog_name".split()

    def get_catalog_name(self, product):
        return product.catalog_name

    def get_brand_name(self, product):
        return product.brand_name

    def get_sub_catalog_name(self, product):
        return product.sub_catalog_name

    def get_image_catalog(self, product):
        return product.catalog.image


    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        data['catalog_image'] = request.build_absolute_uri(instance.catalog.image).replace("api/v1/products", "media")
    #     data['image2'] = request.build_absolute_uri(instance.image2)
    #     data['image3'] = request.build_absolute_uri(instance.image3)
    #     data['image4'] = request.build_absolute_uri(instance.image4)
        return data