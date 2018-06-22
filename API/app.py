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


@ns.route('/v1/rides/')
class RideList(Resource):
    '''Shows a list of all rides, and lets the driver POST to add new tasks'''
    @ns.doc('list_rides')
    @ns.marshal_list_with(store)
    def get(self):
        '''List all rides'''
        return ride.rides

    @ns.doc('create_ride')
    @ns.expect(store)
    @ns.marshal_with(store, code=201)
    def post(self):
        '''Create a new ride'''
        return ride.create(api.payload), 201


@ns.route('/v1/ride/<int:id>')
@ns.response(404, 'Ride not found')
@ns.param('id', 'The ride identifier (id) ')
class Ride(Resource):
    '''Show a single ride  and lets you delete them'''
    @ns.doc('get_store')
    @ns.marshal_with(store)
    def get(self, id):
        '''Fetch a given resource with a given id'''
        return ride.get(id)

    @ns.doc('delete_store')
    @ns.response(204, 'store deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        ride.delete(id)
        return '', 204

    @ns.expect(store)
    @ns.marshal_with(store)
    def put(self, id):
        '''Update a task given its identifier'''
        return ride.update(id, api.payload)


@ns.route('/v1/ride/<int:id>/requests')
@ns.response(404, 'Ride not found')
@ns.param('id', 'The ride identifier (id) ')
class RideRequest(Resource):
    '''Make a request to join a ride'''
    @ns.doc('Join a ride')
    @ns.expect(join_requests)
    @ns.marshal_with(join_requests, code=201)
    def post(self, id):
        '''Create a new ride'''
        return ride.create(api.payload), 201

