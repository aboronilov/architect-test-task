from rest_framework import serializers

from base.models import Base


class AllBasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = "__all__"
