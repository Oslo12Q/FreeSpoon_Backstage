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


class AjaxSourceTable(Table):

    id = Column(field = 'id')
    title = Column(field = 'title')
    reseller_mob = Column(field = 'reseller_mob')
    receive_mode = Column(field = 'receive_mode')
    start_time = Column(field = 'start_time')
    dead_time = Column(field = 'dead_time')
    status = Column(field = 'status')
    volume = Column(field = 'volume')
    details = Column(field = 'details')
    class Meta:
        model = Bulk
        ajax = True
        ajax_source = reverse_lazy('ajax_source_api')

