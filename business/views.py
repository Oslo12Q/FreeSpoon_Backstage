from django.shortcuts import render

# Create your views here.


from .models import *
from table.views import FeedDataView
from business.tables import (
    AjaxSourceTable
)


class MyDataView(FeedDataView):

    token = AjaxSourceTable.token

    def get_queryset(self):
        return super(MyDataView, self).get_queryset()


