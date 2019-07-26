from django.test import TestCase
from .models import UserData
from .models import UserConsumption
from .models import TotalConsumption
from django.utils import timezone
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta

# Models Test


class UserDataTest(TestCase):

    def create_userdata(self, user_id=1, area="a1", tariff="t1"):
        return userdata.objects.create(user_id=user_id, area=area, tariff=tariff)

    def test_userdata_creation(self):
        ud = self.create_userdata()
        self.assertTrue(isinstance(ud, UserData))


class UserConsumption(TestCase):

    def create_userconsumption(self, user_id=1, datetime=datetime(2016, 7, 15, 0, 0, 0), consumption=234.0):
        return userconsumption.objects.create(user_id=user_id, datetime=datetime, consumption=consumption)

    def test_userconsumption_creation(self):
        uc = self.create_userconsumption()
        self.assertTrue(isinstance(uc, UserConsumption))


class TotalConsumption(TestCase):

    def create_totalconsumption(self, datetime=datetime(2016, 7, 20, 0, 0, 0), total_consumption=342.0):
        return totalconsumption.objects.create(datetime=datetime, total_consumption=total_consumption)

    def test_totalconsumption_creation(self):
        tc = self.create_totalconsumption()
        self.assertTrue(isinstance(tc, TotalConsumption))
