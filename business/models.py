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


class Order(models.Model):
	id = models.CharField(max_length=200, primary_key=True)
	mob = models.CharField(max_length=20, null=True, blank=True)
	user_id = models.IntegerField(max_length=11)
	bulk = models.ForeignKey('Bulk')
	receive_mode = models.IntegerField(max_length=11, default=2)
	storages = models.CharField(max_length=11)
        payment_method = models.CharField(max_length=11)
	payment_id = models.IntegerField(max_length=11)
        payment_time = models.DateTimeField()
 	logistics = models.IntegerField(max_length=11)
        detailed = models.CharField(max_length=11)
	payment_price = models.IntegerField(max_length=11)
	
	receive_name = models.CharField(max_length=200, null=True, blank=True)
	receive_mob = models.CharField(max_length=20, null=True, blank=True)
	receive_address = models.TextField(null=True, blank=True)
	status = models.IntegerField(max_length=11)
	freight = models.IntegerField(max_length=11)
	total_fee = models.IntegerField(max_length=11)
	seq = models.IntegerField(max_length=11, default=0)
	create_time = models.DateTimeField(auto_now=True)
	obtain_name = models.CharField(max_length=100, null=True, blank=True)
	obtain_mob = models.CharField(max_length=20, null=True, blank=True)
	is_delete = models.BooleanField(default=False)
	comments = models.TextField(null=True, blank=True)
	def __unicode__(self):
		return 	self.bulk.title
