from mysite.models import Owner, Pet
from rest_framework import serializers


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet


class OwnerSerializer(serializers.ModelSerializer):
    pet_set = PetSerializer(many=True, required=False)

    class Meta:
        model = Owner
