import secrets

class Bank:
    def __init__(self):
        self.users = {}
        self.bank_balance = 100000000
        self.loan_status = True
        self.loan_amount = 0

    def create_user_account(self, name, email, address, account_type):
        account_number = secrets.SystemRandom().randint(10000, 99999)
        while account_number in self.users:
            account_number = secrets.SystemRandom().randint(10000, 99999)

        user = User(account_number, name, email, address, account_type)
        self.users[account_number] = user
        return user

    def delete_user_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            return True
        return False

    def see_all_user_accounts(self):
        return self.users

    def check_bank_balance(self):
        return self.bank_balance

    def check_total_loan_amount(self):
        return self.loan_amount

    def toggle_loan_feature(self):
        self.loan_status = not self.loan_status

    def take_loan(self, user, loan_amount):
        if self.loan_status and self.bank_balance >= loan_amount and user.can_take_loan():
            self.bank_balance -= loan_amount
            self.loan_amount += loan_amount
            user.take_loan(loan_amount)
            return True
        return False

class User:
    def __init__(self, account_number, name, email, address, account_type):
        self.account_number = account_number
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transactions = []
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdrawal amount exceeded"
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transactions

    def can_take_loan(self):
        return self.loan_count < 2

    def take_loan(self, loan_amount):
        self.balance += loan_amount
        self.loan_count += 1
        self.transactions.append(f"Took a loan of ${loan_amount}")

    def transfer_money(self, target_user, amount):
        if target_user:
            if amount > self.balance:
                return "Insufficient balance for the transfer"
            else:
                self.balance -= amount
                target_user.balance += amount
                self.transactions.append(f"Transferred ${amount} to Account {target_user.account_number}")
                target_user.transactions.append(f"Received ${amount} from Account {self.account_number}")
        else:
            return "Account does not exist"

class Admin(User):
    def __init__(self):
        super().__init__(0, "Admin", "admin@bank.com", "Admin Address", "Admin")
