from pyexpat import model
from sqlite3 import Cursor
import mysql.connector as c

can = c.connect(host="localhost", user= "root", passwd= "P@$$ward1", database= "bank")
Cursor = can.cursor()

def check_Acc():
    Sel_Transact = "select Account_No from customers"
    Cursor.execute(Sel_Transact)
    acc_no = Cursor.fetchall()
    for x in range(0, len(acc_no)):
        new_ele = acc_no[x][0]
        Ac_no.append(new_ele) 
    return Ac_no

def fetch(Acc_No):
    Blanc = "select * from customers where Account_No = ({})".format(Acc_No)
    Cursor.execute(Blanc)
    balance = Cursor.fetchall()
    return balance[0][-1]

def update(b):
    Sel_update = "insert into transactions values ({}, '{}', {}, {}, '{}')".format(b[0], b[1], b[2], b[3], b[4])
    Cursor.execute(Sel_update)
    upd_bal = "update customers set balance = ('{}') where Account_No = ({})".format(b[4], b[0])
    Cursor.execute(upd_bal)
    print(f"You have {action[0]} Rs {action[1]}\nYour updated balance is {b[4]} Rs")
    action.clear()
    can.commit()

def withdrawal(bal):
    withdraw = int(input("Enter the Amount you Want to withdraw: "))
    if withdraw > int(bal):
        print ("                   !....Enter A valid Amount you dont have enough balance....!")
    else:
        emp_ty = ""
        empty_list.append(withdraw)
        empty_list.append(emp_ty)
        bal = int(bal) - withdraw
        empty_list.append(bal)
        action.append(withdraw)
        b = [y if y != "" else "0" for y in empty_list]
        update(b)

def Depositing(bal):
    Deposit = int(input("Enter the amount you want to deposit: "))
    bal = int(bal) + Deposit
    emp_ty = ""
    empty_list.append(emp_ty)
    empty_list.append(Deposit)
    empty_list.append(bal)
    action.append(Deposit)
    b = [y if y != "" else "0" for y in empty_list]
    update(b)
    
empty_list = []
ref_list = ["Acc_No", "Date_of_Transaction", "Withdrawal", "Deposit", "Balance"]
Ac_no = []
action = []
# For Withdrawal
def transact():
    Ac_no = check_Acc()
    Options = int(input("What would you like to do today\nPress 1 to Withdraw\nPress 2 for Deposit\nEnter your selection: "))
    if Options == 1:
        Acc_No = int(input("Enter Your Account No: "))
        print(Ac_no)
        if Acc_No in Ac_no:
            empty_list.clear()
            empty_list.append(Acc_No)
            date_transaction = input("Enter Date: ")
            empty_list.append(date_transaction)
            Ac_no.clear()
            bal = fetch(Acc_No)
            action.append("Withdrawn")
            withdrawal(bal)
        else:
            print("!!!Enter a Valid account Number or Register Your Acoount!!!")
     
# For Deposit
    elif Options == 2:
        Acc_No = int(input("Enter Your Account No: "))
        if Acc_No in Ac_no:
            empty_list.clear()
            empty_list.append(Acc_No)
            date_transaction = input("Enter Date: ")
            empty_list.append(date_transaction)
            Ac_no.clear()
            bal = fetch(Acc_No)
            action.append("Deposited")
            Depositing(bal)
        else:
            print("!!!Enter a Valid account Number or Register Your Acoount!!!")