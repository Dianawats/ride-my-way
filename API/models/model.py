from flask import abort


class Rides_db(object):
    def __init__(self, details, name, status, destination):
        """intiate class db variables"""
        self.counter = 0
        self.details = details
        self.name = name
        self.status = status
        self.destination = destination
        self.rides = []

    def get_all(self):
        ride = {'id':'', 'details':'', 'name':'', 'status':'', 'destination':''}
        self.counter = self.counter + 1
        ride['id'] = self.counter
        ride['details'] = self.destination
        ride['name'] = self.name
        ride['destination'] = self.destination
        self.rides.append(ride)
        return self.rides


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

    # def update(self, id, data):
    #     """used for put and updating of a ride """
    #     ride = self.get(id)
    #     ride.update(data)
    #     return ride

    # def delete(self, id):
    #     """ deletes a ride"""
    #     ride = self.get(id)
    #     self.rides.remove(ride)

