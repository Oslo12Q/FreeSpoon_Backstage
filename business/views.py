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
#        import pdb
#	pdb.set_trace()
	name = self.request.GET['filter[batch_name]']	
	mob = self.request.GET['filter[batch_mob]']
	status = self.request.GET['fileter[batch_status]']
	if name:
	   	return super(MyDataView, self).get_queryset().filter(title = name)
	if mob:
	    	return super(MyDataView, self).get_queryset().filter(reseller_mob = mob)
	if status:
	    	return super(MyDataView, self).get_queryset().filter(status =status)
	

        return super(MyDataView, self).get_queryset()


class OrderView(FeedDataView):
    
    token = OrderTable.token

    def get_queryset(self):

	return super(OrderView,self).get_queryset()
