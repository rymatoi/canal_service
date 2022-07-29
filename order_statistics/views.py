from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django_tables2 import SingleTableView, RequestConfig
from qsstats import QuerySetStats

from order_statistics.models import Order
from order_statistics.tables import OrderTable


def OrdersListView(request):
    orders = Order.objects.order_by('date')
    for_graph = tuple((order.date, order.price_dollar) for order in orders)
    total = sum(order.price_dollar for order in orders)

    table = OrderTable(Order.objects.all())
    RequestConfig(request, paginate={"per_page": 10}).configure(table)

    return render(request, 'order_statistics/order_stats.html', {'table': table, 'values': for_graph, 'total': total})
