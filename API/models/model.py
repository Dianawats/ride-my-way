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

    def create(self, data):
        """ Creates a ride with the provided data """
        ride = data
        # ride['id'] = self.counter = self.counter + 1
        self.counter = self.counter + 1
        ride['id'] = self.counter
        self.rides.append(ride)
        return ride

     def update(self, id, data):
        """used for put and updating of a ride """
        ride = self.get(id)
        ride.update(data)
        return ride

    def delete(self, id):
        """ deletes a ride"""
        ride = self.get(id)
        self.rides.remove(ride)





