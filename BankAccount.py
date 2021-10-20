from random import randint

class BankAccount:
  def __init__(self, full_name, account_number, balance = 0):
    self.full_name = full_name
    self.account_number = account_number
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Amount deposited: ${format(amount, '.2f')}. New balance: ${format(self.balance, '.2f')}")

  def withdraw(self, amount):
    if amount > self.balance:
      overdraft_fee = 10
      self.balance -= overdraft_fee
      print(f"Insufficient funds. Overdraft ${format(overdraft_fee, '.2f')} fee charged. Current balance: ${format(self.balance, '.2f')}")
    else: 
      self.balance -= amount
      print(f"Amount withdrawn: ${format(amount, '.2f')}. New balance: ${format(self.balance, '.2f')}")

  def get_balance(self):
    print(f"Hello, {self.full_name}. Your current balance is ${format(self.balance, '.2f')}.")
    return self.balance

  def add_interest(self):
    annual_interest_rate = 1
    interest_rate = annual_interest_rate / 12 / 100
    interest = self.balance * interest_rate
    self.balance += interest
    print(f"Interest of ${format(interest, '.2f')} added! Current balance: ${format(self.balance, '.2f')}")

  def print_statement(self):
    print(f"{self.full_name}")
    print(f"Account No.: ****{self.account_number[-4:]}")
    print(f"Balance: {format(self.balance, '.2f')}")


def rand_account():
  account_number = ""
  for _ in range(8):
    value = randint(0, 9)
    account_number += str(value)
  return account_number

stanley = BankAccount('Stanley Jeong', rand_account(), 1343)
stanley.deposit(2000)

stanley.withdraw(4000)
stanley.get_balance()
stanley.add_interest()
stanley.print_statement()


# random 8 digit generator