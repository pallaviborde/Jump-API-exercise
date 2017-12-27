

import falcon

from .images import Resource


api = application = falcon.API()

# api = application = falcon.API(middleware=[Validator()])

users = Resource()
api.add_route('/users', users)



