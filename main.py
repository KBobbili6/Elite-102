import random
import mysql.connector



def connect():
    return mysql.connector.connect(user = 'root', database = 'example', password = 'KNoodles101')


#function to create a new account
def newAccount():
    connection = connect()
    cursor = connection.cursor()
    userName = input("Enter full name: ")
    userAccount = random.randint(100000000,999999999)
    print("Your new account number is: " + str(userAccount))
    userPIN = random.randint(10000,99999)
    print("Your new PIN is: " + str(userPIN))

    #allow user to deposit money into their new account
    newBalance = input("Enter amount to deposit: ")

    addData = ("INSERT INTO bankaccount(Name, AccountNumber, PIN, Balance) VALUES(%s, %s, %s, %s)")
    vals = (userName, userAccount, userPIN, newBalance)
    cursor.execute(addData, vals)

    connection.commit()

    cursor.close()
    connection.close()





#function to check balance of a bank account
def checkBalance(pin):
    connection = connect()
    cursor = connection.cursor()
    findBalance = f'SELECT Balance FROM bankaccount WHERE PIN = {pin}'
    cursor.execute(findBalance)
    for row in cursor:
        print(row[0])




#function to deposit money into account
def deposit(pin, amount):
    connection = connect()
    cursor = connection.cursor()
    
    addBalance = "UPDATE bankaccount SET Balance = Balance + %s WHERE PIN = %s"
    vals = (amount, pin)
    cursor.execute(addBalance, vals)
    connection.commit()

    cursor.close()
    connection.close()





#function to withdraw money from account
def withdraw(pin, amount):
    connection = connect()
    cursor = connect.cursor()
    
    addBalance = "UPDATE bankaccount SET Balance = Balance - %s WHERE PIN = %s"
    vals = (amount, pin)
    cursor.execute(addBalance, vals)
    connection.commit()

    cursor.close()
    connection.close()




#function to delete bank account
def deleteAccount(pin):
    connection = connect()
    cursor = connect.cursor()

    account = "DELETE FROM bankaccount WHERE PIN = %s"
    cursor.execute(account, pin)
    connection.commit()

    cursor.close()
    connection.close()



#function to alter pin number
def changePin(pin):
    connection = connect()
    cursor = connect.cursor()

    changed = "UPDATE bankaccount SET PIN = %s WHERE PIN = %s"
    cont = True
    while cont:
        newPin = input("Enter new 5 digit pin: ")
        if (len(str(newPin)) == 5):
            cont = False
    vals = (newPin, pin)
    cursor.execute(changed, vals)

    cursor.close()
    connection.close()




#function to alter name
def changeName(pin):
    connection = connect()
    cursor = connect.cursor()

    changed = "UPDATE bankaccount SET Name = %s WHERE PIN = %s"
    newName = input("Enter name: ")
    vals = (newName, pin)
    cursor.execute(changed, vals)

    cursor.close()
    connection.close()




print("Welcome! \n")

def printChoices():
    print("")
    print("1. Create New Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Delete Account")
    print("6. Change PIN Number")
    print("7. Change Name for Account")
    print("8. Exit")



keepRunning = True
while keepRunning:
    printChoices()
    choice = int(input("Enter choice: "))
    if (choice == 1):
        newAccount()
    elif (choice == 2):
        pin = input("Enter pin number: ")
        checkBalance(pin)
    elif (choice == 3):
        pin = input("Enter pin number: ")
        amount = input("Enter amount to deposit: ")
        deposit(pin, amount)
    elif (choice == 4):
        pin = input("Enter pin number: ")
        amount = input("Enter amount to deposit: ")
        withdraw(pin, amount)
    elif (choice == 5):
        pin = input("Enter pin number: ")
        deleteAccount(pin)
    elif (choice == 6):
        pin = input("Enter pin number: ")
        changePin(pin)
    elif (choice == 7):
        pin = input("Enter pin number: ")
        changeName(pin)
    elif (choice == 8):
        print("Thank you!")
        keepRunning = False
    else:
        print("Invalid Input. Please choose a number between 1 and 8.")

