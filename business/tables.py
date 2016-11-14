#!/usr/bin/env python
# coding: utf-8

import django

if django.VERSION >= (1, 10):
    from django.urls import reverse_lazy
else:
    from django.core.urlresolvers import reverse_lazy

from table.columns import Column
from table.columns.calendarcolumn import CalendarColumn
from table.columns.sequencecolumn import SequenceColumn
from table.columns.imagecolumn import ImageColumn
from table.columns.linkcolumn import LinkColumn, Link, ImageLink
from table.columns.checkboxcolumn import CheckboxColumn

from table import Table
from .models import *
from table.utils import A

class AjaxSourceTable(Table):

    id = Column(field = 'id')
    title = Column(field = 'title')
    reseller_mob = Column(field = 'reseller_mob')
    receive_mode = Column(field = 'receive_mode')
    start_time = Column(field = 'start_time',searchable= False)
    dead_time = Column(field = 'dead_time',searchable = False)
    status = Column(field = 'status')
    volume = Column(field = 'volume')
    details = Column(field = 'details')
    class Meta:
        model = Bulk
        ajax = True
        ajax_source = reverse_lazy('ajax_source_api')




class OrderTable(Table):
    
    id = Column(field = 'id')
    mob = Column(field = 'mob')
    user_id = Column(field = 'user_id')
    receive_name = Column(field = 'receive_name')
    receive_mode = Column(field = 'receive_mode')
    payment_price = Column(field = 'payment_price')
    status = Column(field = 'status')
    payment_method = Column(field = 'payment_method')
    payment_id = Column(field = 'payment_id')
    payment_time = Column(field = 'payment_time',searchable= False)
    create_time =Column(field = 'create_time',searchable= False)
    detailed = Column(field = 'detailed')
    receive_address = Column(field = 'receive_address')
    comments = Column(field = 'comments')
    logistics = Column(field = 'logistics')
    
    class Meta:
	model = Order
	ajax = True
	ajax_source = reverse_lazy('ajax_order_api')
