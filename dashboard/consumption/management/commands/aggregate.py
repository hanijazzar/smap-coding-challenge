from django.core.management.base import BaseCommand
from consumption.models import UserData
from consumption.models import UserConsumption
from consumption.models import TotalConsumption
import csv
import os
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'aggregate data'

    def handle(self, *args, **options):
        print("Getting and saving total consumption of all users per time interval...")
        # loop over the dates in 30 min interval
        # for each date, do a query to get all the consumption in that date,
        # then store the sum in a single field total_consumption on that date
        initial_datetime_str = '2016-07-15 00:00:00'
        final_datetime_str = '2016-12-31 23:30:00'

        # datetime(year, month, day, hour, minute, second)
        initial_datetime = datetime(2016, 7, 15, 0, 0, 0)
        current_datetime = datetime(2016, 7, 15, 0, 0, 0)
        final_datetime = datetime(2016, 12, 31, 23, 30, 0)

        initial_datetime_plus30 = initial_datetime + timedelta(minutes=30)
        # print(initial_datetime)
        # print(initial_datetime_plus30)

        while(1):

            total = 0
            # get all the consumptions for current datetime
            timedata_consumption = UserConsumption.objects.filter(
                datetime=current_datetime)

            # loop over consumption per day
            for timedata in timedata_consumption:
                total = total + timedata.consumption

            # add the total consumption per day to a new entry in the database
            _, created = TotalConsumption.objects.get_or_create(
                datetime=current_datetime,
                total_consumption=total,
            )

            # print("Total Consumption for datetime " + str(current_datetime) + " is: " + str(total))

            current_datetime = current_datetime + timedelta(minutes=30)

            # stop the loop once we have passed through all the dates and saved all the totals
            if current_datetime == final_datetime:
                break
        print("Done")
