from email import header
import email
import imp
from msilib.schema import tables
from re import L
import sqlite3
from tkinter import E
from winreg import DeleteValue
from wsgiref import headers
import banking
from database import deleterecord
import permutation
import random
connect = sqlite3.connect("User.db")

# def createDB():
#     connect = sqlite3.connect("User.db")
#     cursorTab = connect.cursor()
#     cursorTab.execute("""CREATE TABLE bankdetails(
#     first_name text,
#     last_name text,
#     gender text,
#     date_of_birth text,
#     state text,
#     country text,
#     email_address text,
#     phone_number int,
#     acct_no text
#     )
#     """)
#     print("Compiled successfully")
# createDB()

def insertInto():
    """Returns new records inserted into the db"""
    print("""Welcome to Ella's mobile banking app! Fast and safe cash transactions. We are happy that you've decided to"""\
    """create an account with us """)
    first_name = input("Hi there!, what's your first name: ")
    last_name = input("What's your last name: ")
    gender = input("What's your gender: ")
    date_of_birth = input("What day were you born: dd-mm-yyy ")
    state = input("What state are you from?: ")
    country = input("What country are you from: ")
    email_address = input("What's your email address: ")
    phone_number= input("What's your phone number: ")
    print("Thank you for filling this information correctly, your account number will be generated shortly")
    accountlist = permutation.accountperm()
    computerrandom = random.choice(accountlist)
    print(f"Your account number is {computerrandom}, ensure you keep it!")
    cursorTab = connect.cursor()
    cursorTab.execute("""INSERT INTO bankdetails VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
    (first_name, last_name, gender, date_of_birth, state, country, email_address, phone_number, computerrandom))
    print("compiled successfully")
    createacctdb()
    fetchall(email_address)
    connect.commit()
# insertInto()
# def seeTable():
#     cursorTab = connect.cursor()
#     cursorTab.execute("""SELECT sql FROM sqlite_master 
#         WHERE tbl_name = 'bankdetails' AND type = 'table';
#         PRAGMA table_info(table_name);
# """)
# seeTable()


def newBalance():
    """Ensure all existing users balances is set to zero once created"""
    cursorTab = connect.cursor()
    cursorTab.execute("""UPDATE acctinfo SET acct_balance = 0""")
    connect.commit()
    # print("Change made successfully")

def fetchall(email_address):
    """Fetch all the data of a specific person"""
    cursorTab = connect.cursor()
    cursorTab.execute("SELECT * FROM acctinfo WHERE email_address = (?)", (email_address,))
    # rowId = cursorTab.fetchall()
    # print(rowId)
    items = cursorTab.fetchone()
    account_list = ["First Name: ", "Last Name: ", "Email Address: ", "Account Number: ", "Account Balance: $"]
    for i in range(len(items)):
        print(account_list[i] + str(items[i]))
    # cursorTab.execute("SELECT * FROM bankdetails WHERE rowid = (?)", (str((rowId,))))
    # items  = cursorTab.fetchone()
    # print("Your new account details are displayed below: ")
    # for item in items:
    #     print(item)
    connect.commit()
# fetchall("davemacbeth@web.com")

def createacctdb():
    """Collect the users bank details of firstname, lastname, emailaddress and account number from the bankdetails database
    This table stores the users info and account balance"""
    # First step, create a new table in the same database that has the bank details
    cursorTab = connect.cursor()
    # Inset or pull the data from the original table into this new table
    cursorTab.execute("""INSERT INTO acctinfo(first_name, last_name, email_address, acct_no) SELECT first_name, last_name, email_address, acct_no FROM bankdetails""")
    print("Account status creation: Successful")
    newBalance()
    # fetchall()
    connect.commit()
    # cursorTab.execute("""CREATE TABLE acctinfo(
    #     first_name text,
    #     last_name text,
    #     email_address text,
    #     acct_no text,
    #     acct_balance int
    # )
    # """)
    # print("Table created successfully")
# createacctdb()

def retrieveCustomerDetails(first_name, last_name, email_address):
    """Retrieve the customer's account details using their email address"""
    cursorTab = connect.cursor()
    print("Thanks for coming in today, your account details will be processed shortly")
    placeholder = cursorTab.execute("""SELECT * FROM acctinfo WHERE email_address = (?)""", (email_address,))
    items = cursorTab.fetchall()
    if (len(items)) == 0:
        print("Sorry one of user details has been entered incorrectly, try again")
        userTransaction = input("Will you like to try again: ")
        if userTransaction == "yes":
            updateCustomer()
            exit()
        else:
            userTransaction = input("Will you like to create an account with us? ")
            if userTransaction == "yes":
                createacctdb()
            else:
                print("Thank you for stopping by at Ella's banking, we hope to see you soon")
                exit()
    else:
        items = cursorTab.fetchone()
        account_list = ["First Name: ", "Last Name: ", "Email Address: ", "Account Number: ", "Account Balance: $"]
        for i in range(len(items)):
            print(account_list[i] + str(items[i]))
            # i += 1
    connect.commit()

def viewBalance(email_address):
    """Enables user to view only their balance"""
    cursorTab = connect.cursor()
    print("Thanks for coming in today, your available balance will be processed shortly")
    cursorTab.execute("""SELECT * FROM acctinfo WHERE email_address = (?)""", (email_address,))
    # if (placeholder) == None:
    #     return "Sorry Incorrect user details"
    # else:
    items = cursorTab.fetchone()
    account_list = ["First Name: ", "Last Name: ", "Email Address: ", "Account Number: ", "Account Balance: $"]
    for i in range (len(items)):
        print(account_list[i] + str(items[i]))
    userTransaction = input("Will that be all for today: ")
    if userTransaction.lower() == "no" or userTransaction.lower() == "n":
        first_name = items[0]
        last_name = items[1]
        email_address = items[2]
        performTransactions(first_name, last_name, email_address)
    else:
        print(f"That will be all for today, thank you for coming. We hope to see you soon!")
    connect.commit()
    exit()

def withdrawal(first_name, last_name, email_address):
    """Withdraws money from the account and shows the remaining balance"""
    withdrawalAmt = (float(input("How much will you like to withdraw: ")))
    cursorTab = connect.cursor()
    cursorTab.execute("""SELECT acct_balance FROM acctinfo WHERE email_address = (?)""", (email_address,))
    acct_balance = (cursorTab.fetchone())[0]
    if withdrawalAmt > acct_balance:
        print(f"Sorry your account balance is too low | Balance available is ${acct_balance}")
        viewBalance(email_address)
    else:
        acct_balance = acct_balance - withdrawalAmt
        cursorTab.execute("""UPDATE acctinfo SET acct_balance = (?) WHERE email_address = (?)""", (acct_balance, email_address,))
    userTransaction = input("Will you like to view your updated balance: ")
    if userTransaction.lower() == "yes" or userTransaction.lower() == "y":
        viewBalance(email_address)
    userTransaction = input("Will that be all for today: ")
    if userTransaction.lower() =="n" or userTransaction.lower() == "no":
        performTransactions(first_name, last_name, email_address)
    else:
        print(f"That will be all for today, thank you for coming {first_name} {last_name}. We hope to see you soon!")
    connect.commit()
    exit()

def deposit(first_name, last_name, email_address):
    """Deposits money into the account"""
    depositAmt = (float(input("How much money will you like to deposit: ")))
    cursorTab = connect.cursor()
    cursorTab.execute("""SELECT acct_balance FROM acctinfo WHERE email_address = (?)""", (email_address,))
    acct_balance = cursorTab.fetchone()[0]
    acct_balance = acct_balance + depositAmt
    cursorTab.execute("""UPDATE acctinfo SET acct_balance = (?) WHERE email_address = (?)""", (acct_balance, email_address,))
    userTransaction = input("Will you like to view your balance? ")
    if userTransaction.lower() == "yes" or userTransaction.lower() == "y":
        viewBalance(email_address)
    userTransaction = input("Will that be all for today: ")
    if userTransaction.lower() =="n" or userTransaction.lower() == "no":
        performTransactions(first_name, last_name, email_address)
    else:
         print(f"That will be all for today, thank you for coming {first_name} {last_name}. We hope to see you soon!")
    connect.commit()
    exit()

def closeAcct(first_name, last_name, email_address):
    """Deletes the account from records"""
    cursorTab = connect.cursor()
    print(f"""We're sorry to see you go but be aware that you are to withdraw all funds from the account you wish to close""" \
        """before closing. Failure to do so will mean loss of funds. Thank you for your patience and understanding"""\
        f"""{first_name} {last_name}.""")
    deleteAcct = input("Are you sure you still want to close your account: ")
    if deleteAcct == "y" or deleteAcct == "yes":
        cursorTab.execute("""DELETE FROM bankdetails WHERE email_address = (?) """, (email_address,))
        cursorTab.execute("""DELETE FROM acctinfo WHERE email_address = (?) AND last_name = (?)
        """, (email_address, last_name, ))
        print("Account deleted successfully")
        print(f"""It's sad seeing you leave {first_name} {last_name}. We wish you the best in life and in your transactions""")
        print("Signed Ella Iwalewa, CEO of Ella's Banking 2022")
    else:
        userTransaction  = input("""Yay, we're glad you changed your mind. Is there anything else you'll like"""\
        """to do today ?""")
        if userTransaction == "yes" or userTransaction == "y":
            performTransactions(first_name, last_name, email_address)
        else:
            print("Thank you for always choosing Ella's banking, we value you so much!")
            exit()
    connect.commit()

def performTransactions(first_name, last_name, email_address):
    """The main the main, I want to perform transactions on the account"""
    userTransaction = input("""What transaction will you like to perform today: withdraw to take out; deposit to add more cash;"""\
    """balance to view-balance; close to close-account permanently: """)
    if userTransaction.lower() == "withdraw" or userTransaction.lower() == "w":
        withdrawal(first_name, last_name, email_address)
    elif userTransaction.lower() == "deposit" or userTransaction.lower() == "d":
        deposit(first_name, last_name, email_address)
    elif userTransaction.lower() == "balance" or userTransaction.lower() == "b":
        viewBalance(email_address)
    elif userTransaction.lower() == "close" or userTransaction.lower() == "c":
        closeAcct(first_name, last_name, email_address)


def updateCustomer():
    """Check if the user has an account, if yes, don't update the account balance, if no update account balance to zero"""
    print("""Thank you for stopping by today at Ella's Banking. Please answer the following security questions so you can """\
        """proceed with your transactions.""")
    customerReq = input("Do you have an account with Ella's Banking? yes/no ")
    if customerReq.lower() == "yes":
        first_name = input("What's your registered first name: ")
        last_name = input("What's your registered last name: ")
        email_address = input("What's your registered email address: ")
        retrieveCustomerDetails(first_name, last_name, email_address)
        usertransactions = input(f"Will you like to perform any transactions today, {first_name}: ")
        if (usertransactions.lower() == "yes" or usertransactions.lower() == "balance" or usertransactions.lower() == "withdraw" or usertransactions.lower() == "close"
        or usertransactions == "withdraw"):
            performTransactions(first_name, last_name, email_address)
        else:
            print(f"That will be all for today, thank you for coming {first_name} {last_name}. We hope to see you soon!")
    else:
        insertInto()
    connect.commit()
updateCustomer()



# I don't think the below function is necessary since I already have fetch all
# def displayNewAcct():
#     """Once a new account has been created, all the users details should be displayed for their perusal"""
#     cursorTab = connect.cursor()
#     cursorTab.execute("""SELECT * FROM acctinfo
#     """)

# newBalance()

    # items = list(cursorTab.execute("""INSERT INTO SELECT first_name, last_name, email_address, acct_no FROM bankdetails"""))
    # for item in items:
    #     print(item)
    # print(value)
    # print("")
    # print("Table created successfully")
    # connect.commit()

    # Insert into this new table the specific details from other table 
    # Then there's a new function, that calls itself and asks if the user has an account, if yes then they're adirected
    # to a new function that returns their account number based on their email address, and full name
    # Then these 3 data are passed into this function that the table is created to display all their info, then they're
    # asked what transaction they'll like to perform.

# fetchall()

# tableInfo = list(try db.prepare("PRAGMA table_info(table_name)"))
#     for line in tableInfo:
#         print(line[1]!, terminator: " ")
#     print()
#  catch _ { }
# def selectacctdetails():
#     connect = sqlite3.connect("User.db") 
#     cursorTab = connect.cursor()
#     acct_value = cursorTab.execute("SELECT acct_no FROM bankdetails")
#     email_value = cursorTab.execute("SELECT email_address FROM bankdetails")
#     connect.commit()
#     return acct_value, email_value


# def acctTable():
#     connect = sqlite3.connect("User.db")
#     cursorTab = connect.cursor()
#     cursorTab.execute("CREATE TABLE (email_address text, acct_no text, balance int)")
