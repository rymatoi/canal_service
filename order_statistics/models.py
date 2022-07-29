from django.db import models


class Order(models.Model):
    class Meta:
        db_table = 'order'

    order_number = models.CharField(max_length=10, verbose_name='Заказ, №')
    price_dollar = models.FloatField(verbose_name='Стоимость, $')
    date = models.DateField(verbose_name='Срок поставки')
    price_rubles = models.FloatField(verbose_name='Стоимость, ₽')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.order_number
