import random
class PaymentMethod:
    id_number = random.random
    account_number = ''
    _account_balance = 10000

    def add_to_balance(self, amount):
        self._account_balance += amount

    def deduct_from_balance(self, amount):
        self._account_balance -= amount


class Card(PaymentMethod):
    card_data = 'card'


class BiometricData(PaymentMethod):
    biometric_data = 'bio'


class MobileWallet(PaymentMethod):
    mobile_number = '123456789'


class Credit(PaymentMethod):
    credit_card_number = '987654321'


class Debit(PaymentMethod):
    debit_card_number = '111111111'
