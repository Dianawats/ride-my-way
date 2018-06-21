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

    def test_main_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_user_can_get_all_rides(self):
        """ Test whether we can get all the rides """
        response = self.app.get('api/v1/rides/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bukoto', str(response.data))

    def test_user_can_get_one_request_for_ride(self):
        """ Test whether we can get all the rides """
        response = self.app.get('api/v1/ride/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Fetch person X', str(response.data))

if __name__ == '__main__':
    unittest.main()
