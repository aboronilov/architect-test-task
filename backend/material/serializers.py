from rest_framework import serializers

from material.models import Material


class AllMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"
