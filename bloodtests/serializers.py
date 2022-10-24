from rest_framework import serializers
from .models import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['code', 'name', 'unit', 'lower', 'upper']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.lower and instance.upper:
            representation['ideal_range'] = str(instance.lower) + ' <= value <= ' + str(instance.upper)
        elif instance.lower:
            representation['ideal_range'] = 'value >= ' + str(instance.lower)
        elif instance.upper:
            representation['ideal_range'] = 'value <= ' + str(instance.upper)
        return representation

    def validate(self, data):
        if data.get('upper') is None and data.get('lower') is None:
            raise serializers.ValidationError({'Lower and upper cannot both be null': True})
        elif data.get('upper') is not None and data.get('lower') is not None:
            if data['upper'] < data['lower']:
                raise serializers.ValidationError({"Lower value can't exceed upper value": True})
        return data
