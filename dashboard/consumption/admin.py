# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserData
from consumption.models import UserConsumption
from consumption.models import TotalConsumption

# Register your models here.

admin.site.register(UserData)
admin.site.register(UserConsumption)
admin.site.register(TotalConsumption)
