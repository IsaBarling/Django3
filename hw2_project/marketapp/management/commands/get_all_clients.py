from django.core.management.base import BaseCommand
from marketapp.models import User


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        clients = User.objects.all()
        self.stdout.write(f'{clients}')
