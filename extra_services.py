from vehicle import Vehicle


class ExtraServices:
    @staticmethod
    def clean_internal(vehicle):
        vehicle.clean_internal = True

    @staticmethod
    def clean_external(vehicle):
        if vehicle.expected_hours >= 2:
            vehicle.clean_external = True
        else:
            print("Must be parked for more than two hours")
