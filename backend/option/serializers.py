from rest_framework import serializers

from option.models import Option


class AllOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"
