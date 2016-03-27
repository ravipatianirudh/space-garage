from payment_method import PaymentMethod
from datetime import datetime


class Identity:
    name = ''
    contact_number = ''

    def __init__(self, name, num):
        self.name = name
        self.contact_number = num

    def __init__(self):
        self.name = ''
        self.contact_number = ''

    def pay(self, amount):
        return -1


class Permit(Identity):
    permit_id = ''
    permit_payment = PaymentMethod()

    def __init__(self, name, num, id):
        self.name = name
        self.contact_number = num
        self.permit_id = id

    def __init__(self):
        self.name = ''
        self.contact_number = ''
        self.permit_id = ''


class Hologram(Identity):
    hologram_id = ''
    issue_date_time = datetime

    def __init__(self, name, num, id):
        self.name = name
        self.contact_number = num
        self.hologram_id = id

    def __init__(self):
        self.hologram_id = ''
        self.issue_date_time = datetime.utcnow()
