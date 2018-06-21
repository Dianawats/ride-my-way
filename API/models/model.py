from flask import abort


class Rides_db(object):
    def __init__(self):
        """intiate class db variables"""
        self.counter = 0
        self.rides = []

    def get(self, id):
        """Gets a ride by id"""
        for ride in self.rides:
            if ride['id'] == id:
                return ride
        return abort(404, "Ride {} doesn't exist".format(id))