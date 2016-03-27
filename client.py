from vehicle import Vehicle, Civilian, Military, Ore
from extra_services import ExtraServices


class Client:
    vehicle = Vehicle
    clean_internal = False
    clean_external = False

    def payGarage(self, vehicle):
        vehicle.owner.pay()

    def avail_service(self):
        if self.clean_external:
            ExtraServices.clean_external(self.vehicle)
        if self.clean_internal:
            ExtraServices.clean_internal(self.vehicle)
