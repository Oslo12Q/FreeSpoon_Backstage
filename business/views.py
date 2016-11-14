from django.shortcuts import render

# Create your views here.


from .models import *
from table.views import FeedDataView
from business.tables import (
    AjaxSourceTable,OrderTable
)


class MyDataView(FeedDataView):

    token = AjaxSourceTable.token

    def get_queryset(self):

        return super(MyDataView, self).get_queryset()

class OrderView(FeedDataView):
    
    token = OrderTable.token

    def get_queryset(self):
#        batch_name = request.data.get('batch_name',None)
#	print batch_name
	return super(OrderView,self).get_queryset().filter(title = batch_name)
