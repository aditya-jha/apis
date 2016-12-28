# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-28 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0058_auto_20161227_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerFireBaseToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_id', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Buyer')),
            ],
            options={
                'verbose_name': 'Buyer FireBase Token',
                'verbose_name_plural': 'Buyer FireBase Tokens',
            },
        ),
    ]
