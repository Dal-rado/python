class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount}KES sent to{recipient}")
        else:
            print("Insufficient amount to send money")


class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, idno):
        self.account_balance = account_balance
        self.phone_number = phone_number
        self.idno = idno

    def buyairtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount

        print(f"{amount}KES airtime bought successfully")


class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name
        self.account_balance += amount
        print(f"{amount}KES received from a customer")
personal = PersonalMpesa(account_balance=100, phone_number=722585042, idno=23005034)
personal.send_money(amount=300, recipient=7256895)
personal.buyairtime(150)
