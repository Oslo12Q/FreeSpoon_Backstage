from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bulk(models.Model):
        title = models.CharField(max_length=200)
        category = models.CharField(max_length=11)
        details = models.TextField()
        reseller = models.CharField(max_length=11)
        reseller_mob = models.CharField(max_length=11)
        storages = models.CharField(max_length=11)
        products = models.CharField(max_length=11)
        start_time = models.DateTimeField()
        dead_time = models.DateTimeField()
        arrived_time = models.CharField(max_length=100, null=True)
        status = models.IntegerField(max_length=11)
        location = models.CharField(max_length=100)
        receive_mode = models.IntegerField(max_length=11, default=2)
        seq = models.IntegerField(max_length=11, default=0)
        card_title = models.CharField(max_length=100)
        card_desc = models.CharField(max_length=255)
        card_icon = models.ImageField(upload_to='images/card_icon/%Y/%m/%d', blank=True)
        create_time = models.DateTimeField(auto_now=True)
        volume = models.CharField(max_length=200)
	def __unicode__(self):
                return self.title

