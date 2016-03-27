from vehicle import Vehicle, Civilian, Military, Ore
from datetime import datetime


class TimeManager:
    elapsed_hours = 0
    penalty_hours = 0
    vehicle = Vehicle
    start_time = datetime
    end_time = datetime

    def __init__(self):
        self.start_time = datetime.utcnow()
        self.elapsed_hours = 0
        self.penalty_hours = 0
        self.vehicle = Vehicle
        self.start_time = datetime.utcnow()

    def __init__(self,vehicle):
        self.start_time = datetime.utcnow()
        self.elapsed_hours = 0
        self.penalty_hours = 0
        self.vehicle = vehicle
        self.start_time = datetime.utcnow()

    def set_start(self):
        self.start_time = datetime.utcnow()

    def set_end(self):
        self.end_time = datetime.utcnow()

    def calculate_hours(self):
        self.elapsed_hours = (self.start_time - self.end_time).total_seconds() / 60 / 60
        if self.elapsed_hours > 6:
            self.penalty_hours = self.elapsed_hours - 6
            self.elapsed_hours -= 6
            if self.penalty_hours > 6:
                self.vehicle.tow = True