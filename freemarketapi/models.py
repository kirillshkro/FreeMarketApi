from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, db_index=True,
                             verbose_name='Наименование')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False,
                                verbose_name='Цена')
    quantity = models.PositiveIntegerField(null=False, verbose_name='Количество')
    description = models.TextField(null=False, blank=True)
    image = models.ImageField(blank=True, null=False, upload_to='images/')
    idx_title = models.Index(fields=('title',))

    def __str__(self):
        return self.title
