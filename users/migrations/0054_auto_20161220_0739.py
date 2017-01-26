# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-20 07:39
from __future__ import unicode_literals

from django.db import migrations

def edit_store_margins(apps, schema_editor):

	Buyer = apps.get_model("users", "Buyer")
	BuyerProductResponse =  apps.get_model("users", "BuyerProductResponse")

	buyers = Buyer.objects.filter(store_global_margin__gt=0)

	for buyer in buyers:
		buyer.store_global_margin = 100
		buyer.save()

	responses = BuyerProductResponse.objects.filter(store_margin__gt=0)

	for response in responses:
		response.store_margin = 100
		response.save()


class Migration(migrations.Migration):

	dependencies = [
		('users', '0053_auto_20161220_0730'),
	]

	operations = [
		migrations.RunPython(edit_store_margins),
	]
