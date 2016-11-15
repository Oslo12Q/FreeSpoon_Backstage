from django.shortcuts import render

from django.db.models import Q

# Create your views here.


from .models import *
from table.views import FeedDataView
from business.tables import (
    AjaxSourceTable,OrderTable
)


class MyDataView(FeedDataView):

    token = AjaxSourceTable.token
    
    def get_queryset(self):

	id = self.request.GET['filter[batch_id]']
	name = self.request.GET['filter[batch_name]']	
	mob = self.request.GET['filter[batch_mob]']
	status = self.request.GET['fileter[batch_status]']

	queryset = super(MyDataView, self).get_queryset()

	if id:
	    queryset = queryset.filter(id = id)
	if name:
	    queryset = queryset.filter(title__contains = name)
	if mob:
	    queryset = queryset.filter(reseller_mob__contains = mob)
	if status:
	    queryset = queryset.filter(status = status)
	return queryset


class OrderView(FeedDataView):
    
    token = OrderTable.token

    def get_queryset(self):

	bulk_id = self.request.GET['filter[batch_id]']	
	number = self.request.GET['filter[order_number]']
        mob = self.request.GET['filter[order_mob]']
	status = self.request.GET['filter[pay_status]']
	method = self.request.GET['filter[pay_method]']
	start_time = self.request.GET['filter[start_day]']
	end_time = self.request.GET['filter[end_day]']

	print start_time
	print end_time
	queryset = super(OrderView,self).get_queryset()

	if bulk_id:
	    queryset = queryset.filter(bulk_id = bulk_id)
	if number:
	    queryset = queryset.filter(id = number)
	if mob:
	    queryset = queryset.filter(mob__contains = mob)
	if status:
	    queryset = queryset.filter(status = status)
	if method:
	    queryset = queryset.filter(payment_method = method)
	if start_time and end_time:
	    queryset = queryset.filter(create_time__range = (start_time,end_time))	
	return queryset
