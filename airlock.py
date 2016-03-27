from vehicle import Vehicle

class Airlock:
    airlock_id = -1
    inner_door_open = False
    outer_door_open = False
    _vehicles_inside = []

    def add_vehicle__from_outer(self,vehicle):
        if len(self._vehicles_inside) < 3:
            self.outer_door_open = True
            self._vehicles_inside.append(vehicle)
            self.outer_door_open = False
        else:
            print("Capacity of airlock " + self.airlock_id + " full.")

    def add_vehicle_from_inner(self,vehicle):
        if len(self._vehicles_inside) < 3:
            self.outer_door_open = True
            self._vehicles_inside.append(vehicle)
            self.outer_door_open = False
        else:
            print("Capacity of airlock " + self.airlock_id + " full.")

    def remove_vehicles(self):
        self._vehicles_inside = []