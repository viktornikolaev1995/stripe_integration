from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.IntegerField(verbose_name='Стоимость', default=0)

    def get_price(self):
        return '{0:2f}'.format(self.price / 100)

    def __str__(self):
        return '{} - {}'.format(self.name, self.price)
