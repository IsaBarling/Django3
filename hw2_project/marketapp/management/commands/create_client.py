from django.core.management.base import BaseCommand
from marketapp.models import User


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = User(name='John', email='john@example.com', telcontact='8987654321',
                        adress='Москва ул.Победы д.25 кв.1')
        client.save()
        self.stdout.write(f'{client}')
