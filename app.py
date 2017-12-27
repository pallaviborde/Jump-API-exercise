import falcon
# Import Resource class from images.py
from .images import Resource

api = application = falcon.API()


users = Resource()
api.add_route('/users', users)



