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

    def create(self, validated_data):
        try:
            # print('TTTTTTTTTTEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSST', validated_data.get('code', None))
            obj = Test.objects.get(code=validated_data.get('code', None))
            obj.name = validated_data.get('name', None)
            obj.unit = validated_data.get('unit', None)
            obj.upper = validated_data.get('upper', None)
            obj.lower = validated_data.get('lower', None)
            obj.save()
            return obj
        except Test.DoesNotExist:
            return Test.objects.create(**validated_data)

