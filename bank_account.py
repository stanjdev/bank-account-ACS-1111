from random import randint

# Random 8 digit number generator
def rand_account():
  account_number = ""
  for _ in range(8):
    value = randint(0, 9)
    account_number += str(value)
  return account_number


# BANK_ACCOUNT CLASS
class BankAccount:
  def __init__(self, full_name, account_number, account_type = 'checking', balance = 0):
    self.full_name = full_name
    self.account_number = account_number
    self.account_type = account_type
    self.balance = balance

  # Deposit 
  def deposit(self, amount):
    self.balance += amount
    print('=============================')
    print(f"{self.full_name}, Amount deposited: ${format(amount, '.2f')}. New balance: ${format(self.balance, '.2f')}")
    print('=============================')

  # Withdraw
  def withdraw(self, amount):
    if amount > self.balance:
      overdraft_fee = 10
      self.balance -= overdraft_fee
      print('=============================')
      print(f"Insufficient funds. Overdraft ${format(overdraft_fee, '.2f')} fee charged. Current balance: ${format(self.balance, '.2f')}")
      print('=============================')
    else: 
      self.balance -= amount
      print('=============================')
      print(f"{self.full_name}, Amount withdrawn: ${format(amount, '.2f')}. New balance: ${format(self.balance, '.2f')}")
      print('=============================')

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
    print('============== STATEMENT ===============')
    print(f"Statement for {self.full_name}")
    print(f"Account No.: ****{str(self.account_number)[-4:]}")
    print(f"Balance: ${format(int(self.balance), '.2f')}")
    print('========================================')


# BANK ACCOUNT EXAMPLES
stanley = BankAccount('Stanley Jeong', rand_account(), 1343)
stanley.deposit(2000)
stanley.withdraw(4000)
stanley.get_balance()
stanley.add_interest()
stanley.print_statement()

mitchell = BankAccount('Mitchell Hudson', 31415921, 'checking')
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

# Add interest to all bank accounts
for account in bank:
  account.add_interest()

# BANK ACCOUNT RUNNING PROGRAM
def run_bank_program():
  running = True

  while (running != False):
    user_input = input("Choose an option: \n1. Create account \n2. Get Statement \n3. Deposit \n4. Withdraw \n'q' to quit: \n")
    if user_input == '1':
      name = input('Enter your full name: ')
      account_number = input('Enter an 8 digit account #: ')
      while not account_number.isdecimal() or len(account_number) != 8:
        # Validate for 8 digits only
        account_number = input('Enter an 8 digit account #: ')
      account_type = input('savings or checking? ')
      while account_type != 'savings' and account_type != 'checking':
        # Validate that it must be 'savings' or 'checking'
        account_type = input('savings or checking? ')
      balance = int(input('Enter an initial balance amount: '))
      new_user = BankAccount(name, int(account_number), account_type, balance)
      bank.append(new_user)

    elif user_input == '2':
      account_number = int(input('enter your account number: '))
      for account in bank:
        if account.account_number == account_number:
          account.print_statement()

    elif user_input == '3':
      account_number = int(input('enter your account number: '))
      deposit_amount = int(input('enter the amount to deposit: $'))
      for account in bank:
        if account.account_number == account_number:
          account.deposit(deposit_amount)

    elif user_input == '4':
      account_number = int(input('enter your account number: '))
      withdraw_amount = int(input('enter the amount to withdraw: $'))
      for account in bank:
        if account.account_number == account_number:
          account.withdraw(withdraw_amount)

    elif user_input == 'q':
      running = False

    else: 
      print("invalid input. Try again")
    
# run_bank_program()


""" ======================================================================================================== """
""" ======================================================================================================== """
""" ======================================================================================================== """
# Stretch goal Bank Class:

# BANK CLASS
class Bank:
  def __init__(self, bank_accounts = [
    BankAccount('Stanley Jeong', rand_account(), 800000),
    BankAccount('Spencer Stevens', rand_account(), 32000),
    BankAccount('Randy Marsh', rand_account(), 2390844),
  ]):
    self.bank_accounts = bank_accounts

  def create_account(self, full_name, account_number, account_type = 'checking', balance = 0):
    new_account = BankAccount(full_name, account_number, account_type, balance)
    self.bank_accounts.append(new_account)

  def deposit(self, account_number, deposit_amount):
    for account in self.bank_accounts:
      if account.account_number == account_number:
        account.deposit(deposit_amount)

  def withdraw(self, account_number, withdraw_amount):
    for account in self.bank_accounts:
      if account.account_number == account_number:
        account.withdraw(withdraw_amount)

  def transfer(self, from_account_number, to_account_number, transfer_amount):
    to_account = None
    from_account = None

    for account in self.bank_accounts:
      if account.account_number == from_account_number:
        # If found, store it
        from_account = account
        break
    for account in self.bank_accounts:
      if account.account_number == to_account_number:
        # If found, store it
        to_account = account
        break

    if from_account and to_account:
      from_account.withdraw(transfer_amount)
      to_account.deposit(transfer_amount)
      print(f"{from_account.full_name} transferred ${transfer_amount} to {to_account.full_name}!")
      print("Current Balances Now:")
      from_account.get_balance()
      to_account.get_balance()
    else:
      return print('One or both accounts not found. Transfer stopped.')

  def statement(self, account_number):
    for account in self.bank_accounts:
      if account.account_number == account_number:
        account.print_statement()


# BANK EXAMPLE:
bank_of_stan = Bank([stanley, mitchell, jordan])
bank_of_stan.create_account('Frank Guilds', 32467362, 'checking', 100)
bank_of_stan.create_account('Bobby Fisher', 12345678, 'savings', 3000)
bank_of_stan.statement(32467362)
bank_of_stan.deposit(32467362, 10000)
bank_of_stan.withdraw(32467362, 2000)
bank_of_stan.transfer(32467362, 12345678, 100)

bank_of_stan.statement(31415921)
bank_of_stan.deposit(31415921, 99999999)

