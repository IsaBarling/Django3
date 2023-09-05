from django.core.management.base import BaseCommand
from marketapp.models import User, Product, Order


class Command(BaseCommand):
    help = "Generate fake clients, products and orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = User(name=f'client{i}',
                          email=f'mail{i}@mail.ru',
                          telcontact=898765432+i,
                          adress=f'adress{i}',
                          )
            client.save()
        for j in range(1, count * 5):
            product = Product(name=f'NameProduct{j}',
                              description=f'description from NameProduct{j}',
                              price=0.0, quantity=j)
            product.save()
        for client in User.objects.all():
            order = Order(customer=client)
            order.save()
