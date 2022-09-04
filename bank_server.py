from sqlite3 import Cursor
import mysql.connector as c
from pyexpat import model
import account_creation
import transactions

con = c.connect(host="localhost", user= "root", passwd= "P@$$ward1", database= "bank")
Cursor = con.cursor()

def balance():
    Sel_cust = "select * from customers where account_no = ({})".format(ACC_NO)
    Cursor.execute(Sel_cust)
    Customer = Cursor.fetchall()
    print(f"Your Balance is: {Customer[0][-1]}")

while True:
    txt = "Welcome to XYZ BANK"
    cent = txt.center(180)
    print("\n", cent)
    inpt = int(input("1-> Create an Account\n2-> Perform a Transaction\n3-> Check Balance\n4-> exit\nEnter your Selection: "))
    if inpt == 1:
        create_acc = account_creation.create()
    elif inpt == 2:
        Transact = transactions.transact()
    elif inpt == 3:
        ACC_NO = int(input("Enter your account number: "))
        balance()
    elif inpt == 4:
        break
    else:
        print("!!!Enter a valid selection!!!")