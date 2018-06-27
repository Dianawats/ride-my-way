import os
import unittest
from flask import json

from API.app import app
from API.models.model import Rides_db



class Url_endpoints(unittest.TestCase):
    # setup and teardown of the app

    def setUp(self):
        details = 'Fetch person X'
        name = 'Car pool'
        status = False
        destination = 'Ntinda'
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.ride = Rides_db(details, name, status, destination)
        self.ride.get_all()
        # self.ride = Rides_db()
        # self.ride.create({'task': 'Fetch person X', "name": "Car pool",
                        #   "status": False, "destination": "ntinda"})        

    def tearDown(self):
        """ Teardown method for the unit tests """
        pass

    def test_main_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_user_can_get_all_rides(self):
        """ Test whether we can get all the rides """
        response = self.app.get('api/v1/rides/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ntinda', str(response.data))

    def test_user_can_get_one_request_for_ride(self):
        """ Test whether we can get a single ride details """
        response = self.app.get('api/v1/ride/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Car pool', str(response.data))


    def test_driver_can_create_a_ride(self):
        """ Test whether we can create a ride """
        dummy_data = {
            "id":'0',
            "details": "car carpool",
            "name": "request car ride",
            "status": False,
            "destination": "I am going to kamwokya"
        }
        response = self.app.post('api/v1/rides/', data=json.dumps(dummy_data),
                                    content_type='application/json',)
        self.assertEqual(response.status_code, 201)
        self.assertIn('I am going to kamwokya', str(response.data))

    def test_passenger_can_request_to_join_a_ride(self):
        """ Test whether we can create a ride """
        request_data = {
            'id':'1',
            'join_details':'I want to join your ride'
        }
        response = self.app.post('api/v1/ride/1/requests', data=json.dumps(request_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('I want to join your ride', str(response.data))


if __name__ == '__main__':
    unittest.main()
