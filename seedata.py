import sqlite3
import customerdb
connect = sqlite3.connect("User.db")
def seeTable():
    cursorTab = connect.cursor()
    cursorTab.execute("""SELECT * FROM bankdetails
""")