import json,uuid
from bank_acc import BankAccount
from data import load_json,write_json,to_dict
from tran import Transaction
import datetime

class Customer():

    def __init__(self,cust_id:str,username:str,password:str,role:str):
        self.cust_id=cust_id
        self.username=username
        self.password=password
        self.role=role
    
    #customer object must be formed to get bank id.
    def get_bankid(self)->str:
        relations=load_json("database/relation.json")
        for relation in relations:
            if(relation["cust_id"]==self.cust_id):
                break
        return relation["bank_acc_id"]

    #withdrawal
    def withdraw_amt(self):
        bank_acc_id=self.get_bankid()
        # BankAccount object must be formed to get credentials of the bank_acc db using bank_id: for eg. balance, fullname.
        # Then manipulate the balance value accordingly.
        b=BankAccount(bank_acc_id)
        balance=b.get_balance()
        min_balance=500
        while True:
            amount=float(input("\nEnter the amount to withdraw: "))
            if(amount<500):
                print("Minimum withdraw amount NPR 500.")
                choice=input("Press 'y' to continue withdraw. Press 'n' to cancel.\nEnter choice: ")
                if(choice=='n'):
                    break
            elif(amount<=balance-min_balance):
                new_balance=balance-amount
                if(b.withdraw(new_balance)):
                    print(f"\nDear {b.get_fullname()}, Your Account: {bank_acc_id} has been debited by NPR: {amount}\nAvailable Balance is NPR: {new_balance}") 
                    break
            else:
                choice=input(f"\nNo sufficient amount for withdrawal.\nAvailable Balance: NPR {balance}\nMinimum existing balance should be NPR 500.\nPress 'y' to continue deposit. Press 'n' to cancel.\nEnter choice: ")
                if(choice=='n'):
                    break
            
    #deposit
    def deposit_amt(self):
        bank_acc_id=self.get_bankid()
        b=BankAccount(bank_acc_id)
        balance=b.get_balance()
        min_deposit=500
        while True:
            amount=float(input("Enter the amount to deposit:"))
            if(amount<500):
                choice=input("Minimum deposit amount should be NPR 500.\nPress 'y' to continue deposit. Press 'n' to cancel.\nEnter choice: ")
                if(choice=='n'):
                    break
            else:
                new_balance=balance+amount
                if(b.deposit(new_balance)):
                    print(f"\nDear {b.get_fullname()}, Your Account: {bank_acc_id} has been credited by NPR: {amount}\nAvailable Balance is NPR: {new_balance}") 
                    break

    #checking balance
    def check_balance(self):
        bank_acc_id=self.get_bankid()
        b=BankAccount(bank_acc_id)
        print(f"Your current balance is: NPR {b.get_balance()}")

    def check_acc_details(self):
        bank_acc_id=self.get_bankid()
        b=BankAccount(bank_acc_id)
        b.get_details()