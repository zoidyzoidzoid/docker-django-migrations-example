from socket import gethostname

from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets

from mysite.models import Owner, Pet
from mysite.serializers import OwnerSerializer, PetSerializer


def info(request):
    data = {
        'version': settings.VERSION,
        'hostname': gethostname(),
    }
    return JsonResponse(data)


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
