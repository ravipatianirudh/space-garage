from vehicle import Vehicle

class Airlock:
    airlock_id = -1
    inner_door_open = False
    outer_door_open = False
    vehicles_inside = []

    def __init__(self,id):
        self.airlock_id = id
        self.inner_door_open = False
        self.outer_door_open = False
        self.vehicles_inside = []

    def add_vehicle__from_outer(self,vehicle):
        if len(self.vehicles_inside) < 3:
            self.outer_door_open = True
            self.vehicles_inside.append(vehicle)
            self.outer_door_open = False
        else:
            print("Capacity of airlock " + self.airlock_id + " full.\n")

    def add_vehicle_from_inner(self,vehicle):
        if len(self.vehicles_inside) < 3:
            self.inner_door_open = True
            self.vehicles_inside.append(vehicle)
            self.inner_door_open = False
        else:
            print("Capacity of airlock " + self.airlock_id + " full.\n")

    def remove_vehicles(self):
        self.vehicles_inside = []