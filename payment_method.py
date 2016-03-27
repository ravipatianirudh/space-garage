class PaymentMethod:
    id_number = ''
    account_number = ''
    _account_balance = -1

    def add_to_balance(self, amount):
        self._account_balance += amount

    def deduct_from_balance(self, amount):
        self._account_balance -= amount


class Card(PaymentMethod):
    card_data = ''


class BiometricData(PaymentMethod):
    biometric_data = ''


class MobileWallet(PaymentMethod):
    mobile_number = ''


class Credit(PaymentMethod):
    credit_card_number = ''


class Debit(PaymentMethod):
    debit_card_number = ''
