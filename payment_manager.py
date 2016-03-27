class PaymentManager:
    total_payment = 0
    fine = 0
    tax = 0
    services_payment = 0
    parking_payment = 0

    def set_amounts_to_vehicle(self, vehicle):
        self.total_payment = vehicle.amount_to_pay
        self.fine = vehicle.fine_payment
        self.parking_payment = vehicle.park_payment
        self.tax = vehicle.tax_payment
        self.services_payment = vehicle.service_payment

    def calculate_fine(self, time_manager):
        self.fine = time_manager.penalty_hours * 24 * 10

    def calculate_parking_payment(self, time_manager):
        self.parking_payment = time_manager.elapsed_hours * 10

    def calculate_tax(self):
        self.tax = (self.fine + self.parking_payment + self.services_payment) * 0.15

    def calculate_total(self):
        self.total_payment = self.fine + self.services_payment + self.parking_payment + self.tax
