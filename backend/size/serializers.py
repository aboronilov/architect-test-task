from rest_framework import serializers

from size.models import Size


class AllSizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"
