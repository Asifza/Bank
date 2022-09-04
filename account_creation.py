from pyexpat import model
from sqlite3 import Cursor
import mysql.connector as c
import transactions
import random

cun = c.connect(host="localhost", user= "root", passwd= "P@$$ward1", database= "bank")
Cursor = cun.cursor()

dummy_list = ["First Name", "Last Name", "Account Type", "Account No", "Contact", "Address", "Adhar", "Pan", "Date of opening", "Balance"]
app_endlist = []
def create():
    x = 0
    m = "0"
    while x < (len(dummy_list)-1):
        if x == 3:
            Accno = random.randint(900000000, 999999999)
            app_endlist.append(Accno)
            x += 1
        else:
            print(f"Enter {dummy_list[x]}: ", end='')
            z = input()
            if z == "Exit" or z == "exit":
                break
            elif z == "Edit" or z == "edit":
                x -= 1
                app_endlist.pop()
            else:
                app_endlist.append(z)
                x += 1
    app_endlist.append(m)
    a = [y if y != "" else "0" for y in app_endlist]
    query = "insert into customers values ('{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}')".format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9])
    try:
        Cursor.execute(query)
    except:
        print("Entry Stopped.....!")
    cun.commit()
    print(f"Congratulations!!! Account Created, Please note down your Acc No for future reference: {Accno} ....!")
    transactions.transact()