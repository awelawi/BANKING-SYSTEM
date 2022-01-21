"""Second customer database that stores their account info and others"""
import sqlite3
connect = sqlite3.connect()
cursorTab = connect.cursor()
cursorTab.execute("""
CREATE TABLE Account_Details
(acct_no text,
user_name text,
)
""")