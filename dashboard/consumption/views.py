# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserData
from .models import UserConsumption
from .models import TotalConsumption

# Create your views here.


def summary(request):
    user_data = UserData.objects.all().order_by('user_id')
    total_consumption = TotalConsumption.objects.all().order_by('datetime')

    context = {
        'message': 'Hello!',
        'data': user_data,
        'total': total_consumption
    }
    return render(request, 'consumption/summary.html', context)


def detail(request):
    context = {
    }
    return render(request, 'consumption/detail.html', context)
