import factory

from mysite import models


class OwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Owner

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('user_name')


class PetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Pet

    name = factory.Faker('name')
