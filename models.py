
import mongoengine as mongo
mongo.connect('test')
import json
# import pymongo 
# db = connection.test

import pymongo
from pymongo import MongoClient

client = MongoClient()

# Get the sampleDB database
db = client.test
record1 = db.user

ct_collection = db.career_timeline
exp_collection = db.experience
import pprint

# Create your models here.
class User(mongo.Document):
    Id = mongo.ObjectIdField
    FirstName = mongo.StringField(max_length=50)
    LastName = mongo.StringField(max_length=50)
    Email = mongo.StringField(required=True)
    CareerTimeline = mongo.ReferenceField
    meta = {'strict': False}

class CareerTimeline(mongo.Document):
    Id = mongo.ObjectIdField
    fromUser = mongo.ReferenceField(User)
    WorkExperience = mongo.EmbeddedDocumentListField
    EducationExperience = mongo.EmbeddedDocumentListField
    Location = mongo.StringField
    meta = {'strict': False}

class Experience(mongo.EmbeddedDocument):
    Id = mongo.ObjectIdField
    fromCareer = mongo.ReferenceField(CareerTimeline)
    Title = mongo.StringField
    StartDate = mongo.DateTimeField
    EndDate = mongo.DateTimeField

collectionName = db.collection_names(include_system_collections=False)

#########################################################################

from bson import json_util
import re
user_ct = db.user.find({},{"CareerTimeline":1})
# print(type(user_ct))
exp_data = {}
for ct in user_ct:
    ct_name = ct["CareerTimeline"]
    # print(ct_name)
    page = open(ct_name, 'r')
    data = json_util.loads(page.read())
    data["fromUser"] = ct_name
    #print(data)
    ct_collection.insert(data)
    
    
    # print(ct_name)
    for sub_title, duration in data['experience'].items():
        exp_data['fromCareer'] = ct_name
        exp_data['Title'] = sub_title
        # print(type(duration))
        if duration:
            delimiters = [" to ", "-", " a ", " bis "]
            regexPattern = '|'.join(map(re.escape, delimiters))
            duration = re.split(regexPattern, duration)
            exp_data['StartDate'] = duration[0]
            exp_data['EndDate'] = duration[1]
            # print(exp_data)
            exp_collection.insert(exp_data)
            exp_data = {}
        else:
            exp_collection.insert(exp_data)
            exp_data = {}

       


    

    
    
    
    


































