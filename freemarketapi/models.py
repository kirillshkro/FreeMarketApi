from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, db_index=True,
                             verbose_name='Наименование')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False,
                                verbose_name='Цена')
    quantity = models.PositiveIntegerField(null=False, verbose_name='Количество')
    description = models.TextField(null=False, blank=True)
    is_selected = models.BooleanField(null=True, default=False)
    order = models.ManyToManyField('Order')

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(null=True)
    product = models.ForeignKey('Product', null=True, related_name='products',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductPhoto(models.Model):
    image = models.ImageField(blank=True, null=False, upload_to='images/')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name


class Order(models.Model):
    user = models.ForeignKey('MarketUser', on_delete=models.CASCADE)
    comment = models.CharField(null=True, max_length=250)
    total_sum = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return f'Order number: {self.pk}'


class MarketUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    phone = models.CharField(max_length=15, blank=False)
