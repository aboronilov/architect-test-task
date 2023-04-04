from rest_framework import serializers

from product.models import Product

from base.serializers import AllBasesSerializer
from material.serializers import AllMaterialsSerializer
from option.serializers import AllOptionsSerializer
from size.serializers import AllSizesSerializer

from base.models import Base
from material.models import Material
from option.models import Option
from size.models import Size


class AllProductsfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "image", "title", "slug", "price"]


class SingleProductSerializer(serializers.ModelSerializer):
    base = serializers.SerializerMethodField()
    material = serializers.SerializerMethodField()
    option = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()

    def get_base(self, obj):
        queryset = Base.objects.all()
        return AllBasesSerializer(queryset, many=True).data

    def get_material(self, obj):
        queryset = Material.objects.all()
        return AllMaterialsSerializer(queryset, many=True).data

    def get_option(self, obj):
        queryset = Option.objects.all()
        return AllOptionsSerializer(queryset, many=True).data

    def get_size(self, obj):
        queryset = Size.objects.all()
        return AllSizesSerializer(queryset, many=True).data

    class Meta:
        model = Product
        fields = [
            "id",
            "image",
            "title",
            "slug",
            "price",
            "base",
            "material",
            "option",
            "size",
        ]
