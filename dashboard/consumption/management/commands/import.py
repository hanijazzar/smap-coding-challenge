from django.core.management.base import BaseCommand
from consumption.models import UserData
from consumption.models import UserConsumption
import csv
import os

class Command(BaseCommand):
    help = 'import data'

    def handle(self, *args, **options):
        # read and store user data
        print("Importing data from csv into SQLite.. this will take some time (around 10mins), please wait...")
        # Todo: catch errors
        path = '../data/'   # path of file
        data_file = path + 'user_data.csv'  # name of file with path
        # open csv file and extract data and map it to UserData model and save them
        with open(data_file) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != 'id':
                    _, created = UserData.objects.get_or_create(
                        user_id=row[0],
                        area=row[1],
                        tariff=row[2],
                        )

        # read and store user consumption
        files_dir = path + 'consumption'

        # loop over the files in the consumption directory
        for filename in os.listdir(files_dir):
            current_user_id = filename.split('.')[0]
            print("Importing consumption data for user: " + current_user_id)
            # open csv file and extract data and map it to UserConsumption model and save them
            with open(files_dir + '/' + filename) as f:
                reader = csv.reader(f)
                for row in reader:
                    #print(row)
                    if row[0] != 'datetime':
                        _, created = UserConsumption.objects.get_or_create(
                            user_id=int(current_user_id),
                            datetime=row[0],
                            consumption=row[1],
                            )
            print("Done Importing consumption data for user: " + current_user_id)
        print("Import complete")
