# Jump-API-exercise

Prerequisits to run this exercise:

python 2.7
nose(For nose test)
mongoDB
To run gunicorn: gunicorn --reload look.app To run an application: http localhost:8000/users?FirstName=<user_name> To run nose tests: nosetests test.py

Steps:
1. Go to the directory where application is saved. Run mongod instance with following command:

mongod

2. Go to the directory where application is saved. Run gunicorn with following command:

gunicorn --reload look.app

3. models.py: This file does not load data into user collection. Open other terminal and go to the folder where users.csv is saved. To load user collection data run following command:

mongoimport -d test -c user --type csv --file users.csv --headerline

4. To load data into careerTimeline and experience collections run models.py.This file runs one time to load data. Please do not run this file more than once as it will duplicate the records.
To run models.py go to directory where it is saved and run with following command:

python models.py

5. Run application with following command:

http localhost:8000/users?FirstName=<user_name>

6. To run nose tests run following command:

nosetests test.py

images.py: This file gets firstname in request and returns json response. app.py: This code creates your WSGI application and aliases it as api.

Please note, I have made few changes in json files. I have removed fullstops(.) from json file to simplify as it was causing a problem while loading data. This can be handled in real time applications, but here to make it little simple I have removed that. Example: Sr. developer, M.Sc.
