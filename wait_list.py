from vehicle import Vehicle


class WaitList:
    vehicles = []

    def __init__(self):
        self.vehicles = []

    def add(self, vehicle):
        self.vehicles.append(vehicle)

    def remove(self, vehicle):
        self.vehicles.remove(vehicle)
