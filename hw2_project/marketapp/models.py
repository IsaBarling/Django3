from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telcontact = models.IntegerField()
    adress = models.CharField(max_length=100)
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.telcontact} {self.adress} {self.date_register}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_load = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.quantity} {self.date_load}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Клиент может иметь несколько заказов.
    products = models.ManyToManyField(
        Product)  # Заказ может содержать несколько товаров.Товар может входить в несколько заказов.
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} {self.total_price} {self.date_ordered}'
