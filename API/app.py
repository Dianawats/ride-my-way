from flask import Flask
from flask_restplus import Api, Resource, fields
from API.models.model import Rides_db


app = Flask(__name__)
api = Api(app, version='1.0', title='Ride-My-Way API',
          description='A carpooling application that provides drivers with the ability to create ride',
          )

ns = api.namespace('api', description='Carpooling operations')

store = api.model('Ride', {
    'id': fields.Integer(readOnly=True, description='The ride unique identifier'),
    'details': fields.String(required=True, description='The ride details'),
    'name': fields.String(required=True, description='The ride name '),
    'status': fields.Boolean(required=False),
    'destination': fields.String(required=True, description='The Destination details')
})

join_requests = api.model('Join', {
    'id': fields.Integer(readOnly=True, description='The ride unique identifier'),
    'join_details': fields.String(required=True, description='The ride details'),

})

ride = Rides_db()
ride.create({'details': 'Fetch person X', "name": "Car pool",
             "status": False, "destination": "ntinda"})
ride.create({'task': 'Fetch person Y', "name": "Car pool",
             "status": True, "destination": "Gulu"})
ride.create({'task': 'Fetch person Z', "name": "Car pool for person Z",
             "status": True, "destination": "Bukoto"})

             

