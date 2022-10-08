import datetime

from Transaction import Transaction
from Account import Account
from Client import Client
from Employee import Employee

clientList = []
customer1 = Client('40', 'Haneen alms', 21, '120221234', '0595454910')
clientList.append(customer1)
customer2 = Client('50', 'Dania Ahmed', 21, '120221674', '0595654910')
clientList.append(customer2)

EmployeeList = []
employee1 = Employee('44', 'Ahmed Mahmoud', 35, '120171201', 'Full time')
EmployeeList.append(employee1)

AccountsList = []
account1 = Account(100, 150, '40')
account2 = Account(200, 280, '50')
account3 = Account(300, 300, '209737293')
AccountsList.append(account1)
AccountsList.append(account2)
AccountsList.append(account3)

idTrans = 0


def deposit():
    global idTrans
    TransObj = Transaction
    accountId = input('Enter the id of Account : ')
    for i in AccountsList:
        if int(accountId) == i.getAccountId():
            customerId = i.getOwnerId()
            for j in clientList:
                if j.getID() == customerId:
                    amount = input('Enter the amount you want to deposit : ')
                    i.setBalance(i.getBalance() + int(amount))
                    TransObj = Transaction(idTrans, datetime.date.today(), j.getID(),
                                           accountId, 'deposit', int(amount))
                    idTrans += 1
                    print("The operation was completed successfully and your balance now is : ")
                    print(i.getBalance())
                    return TransObj


def withdrawal():
    global idTrans
    accountId = input('Enter the id of Account : ')
    for i in AccountsList:
        if int(accountId) == i.getAccountId():
            customerId = i.getOwnerId()
            for j in clientList:
                if j.getID() == customerId:
                    amount = input('Enter the amount you want to withdrawal : ')
                    if i.getBalance() >= int(amount):
                        i.setBalance(i.getBalance() - int(amount))
                        TransObj = Transaction(idTrans, datetime.date.today(), j.getID(),
                                               accountId, 'withdrawal', int(amount))
                        idTrans += 1
                        print("The operation was completed successfully and your balance now is : ")
                        print(i.getBalance())
                        return TransObj


def transfer():
    global idTrans
    TransObj = Transaction
    accountId = input('Enter the ID of the account you want to send from : ')
    for i in AccountsList:
        if int(accountId) == i.getAccountId():
            customerId = i.getOwnerId()
            for j in clientList:
                if j.getID() == customerId:
                    accountId2 = input(
                        'Enter the ID of the account you want to send to : ')
                    for e in AccountsList:
                        if int(accountId2) == e.getAccountId():
                            customerId2 = e.getOwnerId()
                            for m in clientList:
                                if m.getID() == customerId2:
                                    amount = input('Enter the amount you want to transfer : ')
                                    if i.getBalance() >= int(amount):
                                        i.setBalance(i.getBalance() - int(amount))
                                        e.setBalance(e.getBalance() + int(amount))
                                        TransObj = Transaction(idTrans, datetime.date.today(),
                                                               j.getID(), accountId, 'withdrawal',
                                                               int(amount))
                                        idTrans += 1
                                        TransObj = Transaction(idTrans, datetime.date.today(),
                                                               m.getID(), accountId2, 'deposit',
                                                               amount)
                                        idTrans += 1
                                        print("The operation was completed successfully ")
                                        print("account 1 balance is : ")
                                        print(i.getBalance())
                                        print("account 2 balance is : ")
                                        print(e.getBalance())
                                        return TransObj


account_id = 0
client_id = 0


def CreateAccount():
    global account_id
    global client_id
    name = input('Enter your full name : ')
    age = input('Enter your age : ')
    id_no = input('Enter your ID number : ')
    Phone_number = input('Enter your phone number : ')
    clientList.append(Client(client_id, name, age, id_no, Phone_number))
    AccountsList.append(Account(account_id, 0, client_id))
    account_id += 1
    client_id += 1
    print("Your account has been created successfully")


def getbalance():
    accountId = input('Enter the id of Account : ')
    for i in AccountsList:
        if int(accountId) == i.getAccountId():
            customerId = i.getOwnerId()
            for j in clientList:
                if j.getID() == customerId:
                    print('Your balance is :  ')
                    print(i.getBalance())


def menu():
    ("--------------------------------------------------------")
    print("                  Welcome to our bank app              ")
    print("---------------------------------------------------------")
    print("1. Create An Account ")
    print("2. Deposit ")
    print("3. Withdrawal")
    print("4. Transfer to Another Account")
    print("5. View my current balance")
    print("6. Quit")


menu()
global choice
choice = int(input("Enter your choice: "))

while (True):
    if (choice == 1):
        CreateAccount()
        menu()
        choice = int(input("Enter your choice: "))
    elif (choice == 2):
        deposit()
        menu()
        choice = int(input("Enter your choice: "))
    elif (choice == 3):
        withdrawal()
        menu()
        choice = int(input("Enter your choice: "))
    elif (choice == 4):
        transfer()
        menu()
        choice = int(input("Enter your choice: "))
    elif (choice == 5):
        getbalance()
        menu()
        choice = int(input("Enter your choice: "))
    elif (choice == 6):
        break
    if choice > 6 or choice < 1:
        print("Invalid Choice : Please try again.")
        break
