from identity import Identity

class Vehicle:
    id = -1
    expected_hours = -1
    owner = Identity
    make = ''
    model = ''
    slots_taken = -1
    amount_to_pay = -1
    service_payment = -1
    park_payment = -1
    fine_payment = -1
    tax_payment = -1
    tow = False
    clean_internal = False
    clean_external = False


class Civilian(Vehicle):
    def __init__(self):
        self.slots_taken = 1


class Military(Vehicle):
    def __init__(self):
        self.slots_taken = 1


class Ore(Vehicle):
    def __init__(self):
        self.slots_taken = 2
