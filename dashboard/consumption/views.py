# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserData
from .models import UserConsumption

# Create your views here.


def summary(request):
    user_data = UserData.objects.all().order_by('user_id')

    context = {
        'message': 'Hello!',
        'data' : user_data
    }
    return render(request, 'consumption/summary.html', context)


def detail(request):
    context = {
    }
    return render(request, 'consumption/detail.html', context)
