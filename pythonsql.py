import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
connection = create_server_connection("localhost", "root", "PUERTO2003rico++")
print(connection)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
create_database_query = "CREATE DATABASE FOOD"
create_database(connection, create_database_query)


# Type of database I want to create
# Users: NAme, surname, DOB, unique pin Address, ID NO., Email and phone number for their account number
# The requirements for this bank account is that the user enters their Full name, and unique pin to determine if
# It's their account
# Entity for user account, Users only at least for nowmy