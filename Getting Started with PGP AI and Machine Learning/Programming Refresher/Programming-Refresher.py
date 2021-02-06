'''
Created on 26-Jan-2020

@Author: Mohammed Javid

Programming Refresher: Programming Course-End Project
'''

class Bank:
    # parameterized constructor
    def __init__(self, IFSC_Code, bankname, branchname, loc):
        self.ifsc_code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc

class Customer:
    CustomerID = ''
    custname = ''
    address = ''
    contactdetails = ''

class Account(Bank):

    AccountID = ''
    balance = 0
    Cust = Customer()

    def __init__ (self, CustomerID, custname, address, contactdetails, IFSC_Code, bankname, branchname, loc):
        self.Cust.CustomerID = CustomerID
        self.Cust.custname = custname
        self.Cust.address = address
        self.Cust.contactdetails = contactdetails
        self.AccountID = CustomerID
        super(Account,self).__init__(IFSC_Code, bankname, branchname, loc)

    def getAccountInfo(self):
        print ('\n\nCustomerID = ' + self.Cust.CustomerID + '\n')
        print ('custname = ' + self.Cust.custname + '\n')
        print ('address = ' + self.Cust.address + '\n')
        print ('contactdetails = ' + self.Cust.contactdetails + '\n')
        print ('IFSC_Code = ' + self.ifsc_code + '\n')
        print ('bankname = ' + self.bankname + '\n')
        print ('branchname = ' + self.branchname + '\n')
        print ('loc = ' + self.loc + '\n')

    def deposit(self, amount, string):
        self.balance += amount
        print('\nDeposit Success, your Balance is ' + str(self.balance) + '/- \n')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print ('\n\nWithdrawl of Rs:' + str(amount) + '/- is success \n')
            print('Your Balance is ' + str(self.balance) + '\n')
        else:
            print ('You have low balance Rs:' + str(self.balance) + '/- in your account \n')

    def getBalance(self):
        print('\n\n Your balance is ' + str(self.balance) + '\n')

class SavigsAccount(Account):
    SMinBalance = 500
    def __init__ (self, CustomerID, custname, address, contactdetails, IFSC_Code, bankname, branchname, loc):
        super(SavigsAccount,self).__init__(CustomerID, custname, address, contactdetails, IFSC_Code, bankname, branchname, loc)

    def withdraw(self, amount):
        if (amount + self.SMinBalance) <= self.balance:
            self.balance -= amount
            print ('\n\nWithdrawl of Rs:' + str(amount) + '/- is success \n')
            print('Your Balance is ' + str(self.balance) + '\n')
            return
        if amount <= self.balance:
            print ('\nYou should leave minimum balance of Rs:' + str(self.SMinBalance) + '/- in your account. \nPlease check account banalnce to withdraw remaining amount. \n')
        else:
            print ('\nYou have low balance Rs:' + str(self.balance) + '/- in your account \n')

'''
Class NewUser, which accepts inputs from the USER to create Savings Bank account
'''
class NewUser:
    CustomerID = input("Enter your e-mail address:") # Using e-mail as Customer Id, which will be unique
    custname = input("Enter your name:")
    address = input("Enter your address:")
    contactdetails = input("Enter your contact details (i.e your phone number):")

newUser = NewUser()

SActnObj = SavigsAccount(newUser.CustomerID, newUser.custname, newUser.address, newUser.contactdetails, "IDBIK0092K", "IDBI Bank", "Bypass Road", "Madurai")

SActnObj.getAccountInfo()

while(True):
    option = input ("\n\nWould you like to do transaction? press (0/1):(No/Yes)")
    if option == '0':
        break
    if option == '1':
        option = input ('Happy to serve you :), please selct option from below \n1.Deposit \n2.Withdraw \n3.Check Balance \noption:')
    if option == '1':
        amount = input ('Please enter the amount to deposit:')
        SActnObj.deposit(int(amount), 'true')
    if option == '2':
        amount = input ('Please enter the amount to withdraw:')
        SActnObj.withdraw(int(amount))
    if option == '3':
        SActnObj.getBalance()

print ('\n\nThank you so much \n\n')