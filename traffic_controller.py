from garage_manager import GarageManager
from wait_list import WaitList
from airlock import Airlock


class TrafficController:
    num_airlocks = 3
    airlocks = []
    garage_manager = GarageManager
    wait_list = WaitList

    def __init__(self):
        for i in range(0, self.num_airlocks):
            self.airlocks.append(Airlock(i))
        self.wait_list = WaitList
        self.garage_manager = GarageManager

    def __init__(self, garage, wl):
        for i in range(0, self.num_airlocks):
            self.airlocks.append(Airlock(i))
        self.garage_manager = garage
        self.wait_list = wl

    def wait_to_garage(self):
        if len(self.wait_list.vehicles) > 0:
            for i in range(0, len(self.airlocks)):
                if len(self.airlocks[i].vehicles_inside) < 3:
                    self.airlocks[i].add_vehicle_from_outer(self.wait_list.vehicles[0])
                    self.wait_list.vehicles = self.wait_list.vehicles[1:]
                else:
                    print("There's no space in Airlock " + i + "\n")
            for i in range(0, len(self.airlocks)):
                for j in self.airlocks[i].vehicles_inside:
                    error = self.garage_manager.assign_slots(j)
                    self.airlocks[i].vehicles_inside.remove(j)
                    if error == -1:
                        print("The cars will be held in the airlock\n")
                        break
        else:
            print("No one in queue\n")

