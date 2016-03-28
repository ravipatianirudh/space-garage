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
        assigned = False
        for i in range(0,len(self.slots)):
            for j in range(i,i+vehicle.slots_taken):
                if self.slots[j].occupying_vehicle is not None:
                    break
                elif j == i+vehicle.slots_taken - 1:
                    for k in range(i,i+vehicle.slots_taken):
                        self.slots[k] = Slot(k,True,vehicle)
                    assigned = True
        if not assigned:
            print("No Free Space\n")
            return -1

    def return_free_slots(self):
        count = 0
        for i in range(0,len(self.slots)):
            if i.occupying_vehicle is None:
                count += 1
        return count