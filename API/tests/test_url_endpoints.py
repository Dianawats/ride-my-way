import unittest

from API.app import app
from API.models.model import Rides_db


class Url_endpoints(unittest.TestCase):
    # setup and teardown of the app

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.ride = Rides_db()
        self.ride.create({'task': 'Fetch person X', "name": "Car pool",
             "status": False, "destination": "ntinda"})
        # self.ride = Rides_db()
        # self.ride.create({'task': 'Fetch person X', "name": "Car pool",
                        #   "status": False, "destination": "ntinda"})

        self.dummy_data = {

            "details": "car carpool",
            "name": "request car ride",
            "status": False,
            "destination": "I am going to kamwokya"
        }

    def tearDown(self):
        """ Teardown method for the unit tests """
        pass