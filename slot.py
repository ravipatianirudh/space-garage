from vehicle import Vehicle

class Slot:
    slot_id = -1
    occupied = False
    occupying_vehicle = Vehicle

    def __init__(self, id, status, vehicle):
        self.slot_id = id
        self.occupied = status
        self.occupying_vehicle = vehicle