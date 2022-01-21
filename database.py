from distutils.sysconfig import customize_compiler
import sqlite3
from subprocess import list2cmdline
from tkinter.tix import Select

# Create variable to connect to database
connect = sqlite3.connect("Customer.db")
# You can also use a database in memory, but it's not permanent and doesnt save
# conn = sqlite3.connect(":memory:")

# Create a table in sqlite3 is by creating a cursor, which tells the database what you want to do, kinda like given it
# a method

# QUERY the database and return ALL Records
def showAll():
    """Shows all data/fields/query in the database"""
    # Create a cursor
    cursortab = connect.cursor()
    # cursortab.execute("""CREATE TABLE customersdb(
    #                     first_name text,
    #                     last_name, text,
    #                     date_of_birth text,
    #                     house_address text,
    #                     email_address text,
    #                     phone_no int
    # )""")
    # Query the database
    cursortab.execute("SELECT rowid, * FROM customers")
    items = cursortab.fetchall()
    for item in items:
        print(item)

    # Commit the command
    connect.commit()

    # Close our connection, unles you'll be using it elsehwere

    # Retrieve data from the user

# Add a new record to the tables
def addrecord(first, last, dob, house_address, email, phone_no):
    cursortab = connect.cursor()
    cursortab.execute("""INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)""", 
    (first, last, dob, house_address, email, phone_no))
    connect.commit()
    # connect.close()
def deleterecord(lastname):
    cursortab = connect.cursor()
    cursortab.execute(f"DELETE FROM customers WHERE last_name = (?)", lastname)
    connect.commit()

def addmanyrecs(list):
    cursortab = connect.cursor()
    cursortab.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", (list))
    connect.commit()

# lookup with where
def email_adlookup(email):
    cursortab = connect.cursor()
    cursortab.execute("SELECT * FROM customers WHERE email_address = (?)", (email,))
    items = cursortab.fetchall()
    for item in items:
        print(item)














# # Create a table
# cursortab.execute("""CREATE TABLE customers (
#     first_name text,
#     last_name text,
#     date_Of_birth text,
#     house_address text,
#     email_address text,
#     phone_no int
# )""")

# SO I can have more than one table, I'll have one for the account details, and password login info
#data types in SQL
#  NULL
# INTEGER
# REAL
# TEXT
# BLOB

# If you're working with lots of data
# manyData  = [('Wes', 'Brown', 'bcd house','01-01-2001','wesbrown@hi.com', 234567890),
#             ('Dan', 'Mike', 'zero house', '02-01-2001', 'dan@mike.com', 22222222222),
# ]

# cursortab.executemany("INSERT INTO customers VALUES (?,?,?,?,?,?)", manyData)
# Insert 1 data into your table
# cursortab.execute("""INSERT INTO customers VALUES ('Barb', 'Allen', '22-05-2003', 'abc house', 
# 'barballen@gmail.com', 123456789)
# """)

# Query the database
# rowid is primary id
# Searching for or finding cetain items
# % is a placeholder, and like can be used to find like surnames that start with b etc
# cursortab.execute("SELECT last_name FROM customers WHERE last_name LIKE 'U%'")
# So I can use this function/method to find the users account details by finding sqlite their lastname and email address
# ofc I'll use a placeholder for this, then I'll create a command where it only returns the money in their account 
# c.fetchone() fetches one specific one which is the first row in the data
# c.fetchmany(3) fetches more than one where in this case is 3
# fetches all

# Update records
# cursortab.executescript("""UPDATE customers SET house_address = 'bcd house' WHERE last_name = 'Brown';
#                            UPDATE customers SET date_of_birth = '01-01-2001' WHERE last_name = 'Brown';
#                            UPDATE customers SET house_address = 'zero house'WHERE last_name = 'Mike';
#                            UPDATE customers SET date_of_birth = '02-01-2001' WHERE last_name = 'Mike';
# """)
# cursortab.execute("SELECT * FROM customers ORDER BY last_name;")

# Attempt at getting the rowid of certain data
# cursortab.execute("""SELECT phone_no FROM customers WHERE last_name LIKE 'U%' 
# """)

# Delete records or dropped from a table
# cursortab.execute("DELETE from customers WHERE last_name = 'Umoye'")

# Using AND/OR
# cursortab.execute("SELECT * FROM customers WHERE last_name = 'Brown' AND first_name = 'Wes'")

# USING LIMIT
# cursortab.execute("SELECT * FROM customers LIMIT 2")

# DELETE A TABLE
# cursortab.execute("DROP TABLE customers")
# items = (cursortab.fetchall())
# print(items)
# for item in items:
#     print(items)
# for item in items:
#     print(item[0] +"\t\t "+ item[1] +"\t\t "+ item[2])
# for item in items:
#     print(item[0] + " " + item [1] + " " + item[2])
print("Command executed successfully")


# Commit command
# connect.commit()

# close our connection which happens by default
# connect.close()