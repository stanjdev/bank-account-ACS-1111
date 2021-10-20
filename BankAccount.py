from random import randint

class BankAccount:
  def __init__(self, full_name, account_number, account_type = 'checking', balance = 0):
    self.full_name = full_name
    self.account_number = account_number
    self.account_type = account_type
    self.balance = balance

  # Deposit 
  def deposit(self, amount):
    self.balance += amount
    print(f"Amount deposited: ${format(amount, '.2f')}. New balance: ${format(self.balance, '.2f')}")

  # Withdraw
  def withdraw(self, amount):
    if amount > self.balance:
      overdraft_fee = 10
      self.balance -= overdraft_fee
      print(f"Insufficient funds. Overdraft ${format(overdraft_fee, '.2f')} fee charged. Current balance: ${format(self.balance, '.2f')}")
    else: 
      self.balance -= amount
      print(f"Amount withdrawn: ${format(amount, '.2f')}. New balance: ${format(self.balance, '.2f')}")

  # Get Balance
  def get_balance(self):
    print(f"Hello, {self.full_name}. Your current balance is ${format(self.balance, '.2f')}.")
    return self.balance

  # Add Interest
  def add_interest(self):
    annual_interest_rate = 1.2 if self.account_type == "savings" else 1
    interest_rate = annual_interest_rate / 12 / 100
    interest = self.balance * interest_rate
    self.balance += interest
    print(f"Interest of ${format(interest, '.2f')} added! Current balance: ${format(self.balance, '.2f')}")

  # Print Statement
  def print_statement(self):
    print(f"{self.full_name}")
    print(f"Account No.: ****{str(self.account_number)[-4:]}")
    print(f"Balance: ${format(self.balance, '.2f')}")


# Random 8 digit generator
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


mitchell = BankAccount('Mitchell Hudson', 3141592, 'checking')
mitchell.deposit(400000)
mitchell.print_statement()
mitchell.add_interest()
mitchell.print_statement()
mitchell.withdraw(150)
mitchell.print_statement()


jordan = BankAccount('Jordan Michael', rand_account(), 'savings', 100000000)
jordan.deposit(4003000)
jordan.print_statement()
jordan.add_interest()
jordan.print_statement()
jordan.withdraw(150)
jordan.print_statement()


bank = [stanley, mitchell, jordan]

for i in range(len(bank)):
  bank[i].add_interest()
  
running = True

while (running != False):
  user_input = input("Choose an option: \n1. Create account \n2. Get Statement \n3. Deposit \n4. Withdraw \n'q' to quit: ")
  if user_input == '1':
    name = input('Enter your full name: ')
    account_number = input('Enter an 8 digit account #: ')
    balance = input('Enter an initial balance amount: ')
  elif user_input == '2':
    account_number = input('enter your account number: ')
  elif user_input == '3':
    account_number = input('enter your account number: ')
    amount = input('enter the amount to deposit: $')
  elif user_input == '4':
    account_number = input('enter your account number: ')
    amount = input('enter the amount to withdraw: $')
  elif user_input == 'q':
    running = False
  else: 
    print("invalid input. Try again")

