#to generate account numbers
import random

class BankAccount:
  def __init__(self, full_name, balance):
    self.name = full_name
    self.account =  random.randint(9999999,100000000)
    self.balance = balance
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      self.get_balance()
    else:
      print("Cannot deposit a negative amount")

  def withdraw(self, amount):
    if amount > 0 and self.balance - amount > 5:
      self.balance -= amount
      print(f"You have withdrawn {amount}.")
      self.get_balance()
      
    else:
      #I don't think you are able to overdraft from a banking interface.
      #I believe you have to be using your card, or check in a transaction that is taken as credit.
      #a withdrawl process will merely block the transaction, to the best of my knowledge
      print("Sorry, cannot complete your transaction.\nTry checking your balance.")

  def get_balance(self):
    print("Your current balance is:")
    print(f"${self.balance}")

  def add_interest(self):
    self.get_balance()
    interest = self.balance * 0.00083
    self.balance += interest
    self.balance = round(self.balance, 2)
    print("With interest,")
    self.get_balance()
  
  def print_statement(self):
    print(f"Statement:\n{self.name}\nAccount No.: {self.account}\nBalance: ${self.balance}")

#---------------------------------------------------------------------------------------------------------------------------------

becks_account = BankAccount("Beck Haywood", 10)
arthurs_account = BankAccount("Arthur Gerrety", 5)
#just made my friend a millionare
jacksons_account = BankAccount("Jackson", 1000000)

becks_account.print_statement()

arthurs_account.withdraw(10)
arthurs_account.get_balance()
arthurs_account.deposit(10)
arthurs_account.withdraw(10)


jacksons_account.deposit(-20)
jacksons_account.get_balance()
jacksons_account.add_interest()
jacksons_account.print_statement()





#---------------------------------------------------------------------------------------------------------------------------------

#initialize account
mitchells_account = BankAccount("Mitchell", 0)

#override random number
mitchells_account.account = "03141592"

#deposit your app sale
mitchells_account.deposit(400000)

#check on your account
mitchells_account.print_statement()

#create money from nothing
mitchells_account.add_interest()

#see the results
mitchells_account.print_statement()

#get petty cash for yeezys
mitchells_account.withdraw(150)

#keep watching those numbers
mitchells_account.print_statement()

accounts = [becks_account,jacksons_account,arthurs_account,mitchells_account]
#---------------------------------------------------------------------------------------------------------------------------------



def create_account():
  
  #get name
  username = input("Hi, thank you for choosing macSBank!\nTo get started on your online banking journey, Please enter your full name below (Last, First):\n--->  ")
  
  #Isolate first and last for better user experience
  first_and_last = username.split()
  first_name = first_and_last[1]
  last_name = list(first_and_last[0])
  print(last_name)
  del (last_name[-1])
  last_name = "".join(last_name)
  
  consent = input(f"Well then, {first_name},\n  To open an account with us at macSBack we will just need an initial deposit of $5.\nThat $5 must be maintained in order for your account to remain active.\nIf your balance dips below $5, you will have one month to meet the minimum balance.\nIf the minimum balance is not met, then your account will be closed, and all remaining funds will become a part of macSBank.\nDo you agree to these terms? (Y/N)\n---> ")
  if consent == "N":
    print("I'm sorry we couldn't be of more service to you.\nHave a nice day!")
    return
  elif consent == "Y":
    init_deposit = float(input("Now we'll just need your initial deposit, submit it below:\n--->   "))
    if init_deposit >= 5:
      print("You should be all set to start banking!")
      return username, init_deposit
    else:
      print("Sorry, there was an error in creating your account.")

#---------------------------------------------------------------------------------------------------------------------------------

def verify_account(accounts, account_number):
  for i in range(0, len(accounts)):
    if accounts[i].account == account_number:
      print(accounts[i])
      user_account = accounts[i]
      return user_account

#---------------------------------------------------------------------------------------------------------------------------------

def start_banking():
  print("Hi, welcome to macSBank!")
  banking = True
  while banking == True:
    command = input("Enter:\n C to create an account\n D to deposit to an existing account\n W to withdraw from an existing account\n S to view a statement from an existing account\n or, Q to quit.\n")
    if command == "C":
      credentials = create_account()
      new_user_account = BankAccount(credentials[0], credentials[1])
      accounts.append(new_user_account)
      print(f"Your account number is {new_user_account.account}.\nIf you forget your account number your will be locked out of your account, and all funds will be absorbed by macSBank.")
    elif command == "D":
      account_number = input("Input your account number below:\n--->   ")
      user_account = verify_account(accounts, account_number)
      deposit = float(input("How much would you like to deposit?\n--->   "))
      user_account.deposit(deposit)
    elif command == "W":
      account_number = input("Input your account number below:\n--->   ")
      user_account = verify_account(accounts, account_number)
      withdraw = float(input("How much would you like to withdraw?\n--->   "))
      user_account.deposit(withdraw)
    elif command == "S":
      account_number = input("Input your account number below:\n--->   ")
      user_account = verify_account(accounts, account_number)
      user_account.print_statement()
    elif command == "Q":
      print("Have a nice day!")
      banking = False
    else:
      print("Sorry, command not recognized.")

start_banking()
#would like to refine more, but this is what I got