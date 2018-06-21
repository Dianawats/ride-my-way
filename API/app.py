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
