from slot import Slot

class GarageManager:
    capacity = 100
    slots = []

    def __init__(self):
        for i in range(0,self.capacity):
            self.slots.append(Slot(i,False,None))

    def __init__(self,capacity):
        self.capacity = capacity
        for i in range(0,self.capacity):
            self.slots.append(Slot(i,False,None))

    def assign_slots(self,vehicle):
        for i in range(0,len(self.slots)):
            for j in range(i,i+vehicle.slots_taken):
                if(self.slots[j].occupying_vehicle != None):
                    break
                elif j == i+vehicle.slots_taken - 1:
                    for k in range(i,i+vehicle.slots_taken):
                        self.slots[k] = Slot(k,True,vehicle)