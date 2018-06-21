from flask import abort


class Rides_db(object):
    def __init__(self):
        """intiate class db variables"""
        self.counter = 0
        self.rides = []

    