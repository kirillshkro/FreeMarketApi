from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, db_index=True,
                             verbose_name='Наименование')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False,
                                verbose_name='Цена')
    quantity = models.PositiveIntegerField(null=False, verbose_name='Количество')
    description = models.TextField(null=False, blank=True)

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
