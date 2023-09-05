from django.core.management.base import BaseCommand
from marketapp.models import User


class Command(BaseCommand):
    help = "Get client with adress icontains  <adress>."

    def add_arguments(self, parser):
        parser.add_argument('adress', type=str, help='User adress')

    def handle(self, *args, **kwargs):
        adress = kwargs['adress']
        user = User.objects.filter(adress__icontains=adress)
        self.stdout.write(f'{user}')
