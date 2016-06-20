from collections import OrderedDict
from os import environ
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
    ip = environ.get('MY_POD_IP')
    if ip:
        data['ip'] = ip
    data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
    return JsonResponse(data)


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
