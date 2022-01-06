import mysql.connector
sqlobj = mysql.connector.connect(
    host="localhost", password="1234", user="root", database="test")
cursor = sqlobj.cursor()
# cursor.execute("create table abc (name char(20) , username char(20) , itemwon char(20),rupees_donated int(10)")
# con.commit()

bidItems = {}
users = {}


def registration():
    # Take user input for name, username, password
    pass


def login():
    # Take user input for username and password and check from dictionary if username available and password matches
    pass


def mainMenu():
    # write menu options after login as 1. Add item 2. Bid for item 3. Display items 4. Logout
    pass


def displayItems():
    # write a loop to display all items of dictionary
    pass


def bidForItem(user, item, bidprice):
    # check if current price is lower than bid price of item
    pass


def addItemForBid():
    # take user input for item name, price
    pass
