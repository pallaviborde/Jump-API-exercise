import json
import mongoengine as mongo
mongo.connect('test')
import falcon
import pymongo
from pymongo import MongoClient
import pprint
from datetime import datetime
from bson import json_util
import sys

client = MongoClient()
db = client.test
record1 = db.user
ct_collection = db.career_timeline
exp_collection = db.experience
# from mongoengine import *


class Resource(object):
    def search(FirstName):
         return record1.find_one({"First Name": FirstName},{"CareerTimeline":1})['CareerTimeline']

    def on_get(self, req, resp):
        try:
            FirstName = req.get_param("FirstName")
            lst = []
            # json_name = record1.find_one({"First Name": FirstName},{"CareerTimeline":1})['CareerTimeline']
            json_name = Resource.search(FirstName)
            titles = exp_collection.find({"fromCareer": json_name},{"Title": 1, "StartDate": 1})

            for x in titles:
                new_date = datetime.strptime(x['StartDate'].lower(), '%B %Y')
                lst.append(new_date)
                lst = sorted(lst)
            firstExperience = lst[0]
            if isinstance(firstExperience, datetime):
                firstExperience =  firstExperience.isoformat()
            else:
                firstExperience = json.JSONEncoder.default(self, firstExperience)
            # pprint.pprint(firstExperience)
            

            exp = json.dumps(firstExperience, default=json_util.default)




            doc = {
                'users': [
                    {
                        'FirstName': FirstName,
                        # 'FirstExperience': exp[1:8]
                    }

                ]

            }

            # Create a JSON representation of the resource
            resp.body = json.dumps(doc, ensure_ascii=False)

            # The following line can be omitted because 200 is the default
            # status returned by the framework, but it is included here to
            # illustrate how this may be overridden as needed.
            resp.status = falcon.HTTP_200
        except:
            resp.status = falcon.HTTP_404

    


        
