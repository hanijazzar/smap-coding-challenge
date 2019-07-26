# SMAP Python Developer Challenge - Solution by Hani Jazzar

### Approach, Implementation Decisions, and Notes

- App can be run directly as a django project. No external packages were used. Setting up a virtual environment with the django dependicies is all what's needed.
- All the data is already imported and ready to use in db.sqlite3
- Importing of data is done in import.py
- For the implementation of an aggregation for consumption data, I made a file called aggregate.py inside the commands directory next to import.py that stores the total consumption per day of all users in a separate table. Just run `python manage.py aggregate` in order to run it (it is already done and the data is stored)
- The storage of data in sqlite is not very efficient as it is currently made. I suggest that all the consumption data should be stored in a NoSQL database for better effciency and scalability.
- The app should run perfectly without errors. Please let me know if you encounter any issues while running the app.
