# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-08 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_buyerstorelead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerproductlanding',
            name='buyer_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.BuyerProducts'),
        ),
        migrations.AlterField(
            model_name='buyerproductresponsehistory',
            name='buyer_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.BuyerProducts'),
        ),
    ]
