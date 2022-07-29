import django_tables2 as tables
from .models import Order


class OrderTable(tables.Table):
    """ Класс для отображения списка заказов в виде таблицы"""

    class Meta:
        model = Order
        template_name = "django_tables2/bootstrap.html"
        fields = ("order_number", "price_dollar", "date", "price_rubles",)
