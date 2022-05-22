from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.IntegerField(verbose_name='Стоимость', default=0)  # price of item in cents

    def get_price(self):
        return '{0:.2f}'.format(self.price / 100)  # price of item in dollars

    def __str__(self):
        return 'name: {}, price: {}'.format(self.name, self.price)
