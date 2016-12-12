from rest_framework import serializers
from saikor_webservice.models import Saikorian


class SaikorianSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rollNumber=serializers.IntegerField(read_only=False)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    donation = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    description = serializers.CharField(required=False, allow_blank=True,)
    emailId = serializers.EmailField(required=True, allow_blank=False,)

    def create(self, validated_data):
        """
        Create and return a new `Saikorian` instance, given the validated data.
        """
        return Saikorian.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Saikorian` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.rollNumber = validated_data.get('rollNumber', instance.rollNumber)
        instance.name = validated_data.get('name', instance.name)
        instance.donation = validated_data.get('donation', instance.donation)
        instance.description = validated_data.get('description', instance.description)
        instance.emailId = validated_data.get('emailId', instance.emailId)
        instance.save()
        return instance