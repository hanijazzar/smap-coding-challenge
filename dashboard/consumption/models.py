# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserData(models.Model):
    user_id = models.IntegerField()
    area = models.CharField(max_length=50)
    tariff = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user_id) + '-' + self.area + '-' + self.tariff


class UserConsumption(models.Model):
    user_id = models.IntegerField()
    datetime = models.DateTimeField()
    consumption = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return str(self.user_id) + '-' + str(self.datetime) + '-' + str(self.consumption)


class TotalConsumption(models.Model):
    datetime = models.DateTimeField()
    total_consumption = models.DecimalField(decimal_places=2, max_digits=16)

    def __str__(self):
        return str(self.datetime) + '-' + str(self.total_consumption)
