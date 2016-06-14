import random

from django.core.management.base import BaseCommand, CommandError

from mysite.factories import OwnerFactory, PetFactory
from mysite.models import Owner


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument('size', nargs=1, type=int)

    def handle(self, *args, **options):
        size = options.get('size')
        if not size:
            raise CommandError('You need to specify how many owners to create')

        size = size[0]

        self.stdout.write(
            self.style.SUCCESS('Deleting {} owners'.format(Owner.objects.count())))

        Owner.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS('Creating {} owners'.format(size)))

        OwnerFactory.create_batch(size=size)
        for owner in Owner.objects.all():
            for _ in range(random.randrange(1, 5)):
                PetFactory(owner=owner)

        self.stdout.write(
            self.style.SUCCESS('{} owners successfully created!'.format(Owner.objects.count())))

