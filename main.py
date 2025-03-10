import json
from user import Customer
from admin import Admin
from data import load_json,write_json

def auth(username:str,password:str,role:str)->bool:
    users= load_json("database/user_data.json") 
    match = any(user for user in users if user["username"] == username and user["password"] == password and user["role"] == role)
    return match

def get_id(username:str,password:str,role:str):
    data=load_json("database/user_data.json")
    for user in data:
        if user["username"] == username and user["password"] == password and user["role"] == role:

            cust_id=user["cust_id"]
            break
    return cust_id

# main code
role=input("Enter your role (admin/user)? ")
uname=input("Enter username: ")
pw=input("Enter password: ")
match=auth(uname,pw,role)
if(match):
    if role=="admin":
        print(f"Welcome, {uname}! You've logged in as an {role}.")
        a=Admin(get_id(uname,pw,role),uname,pw,role)
        while True:
            try:
                choice=int(input("\nPress keys to proceed:\n1. Add new user\n2. View Users\n3. Exit\nEnter choice: "))
                match choice:
                    case 1:
                        a.create_user()
                    case 2:
                        a.view_users()
                    case 3:
                        print("You've been logged out.")
                        break
                    case _:
                        print("Please enter a valid choice.")
            except ValueError:
                print("Please enter a valid choice.")

    else: #if role=user
        print(f"Welcome, {uname}! You've logged in as a {role}.")
        cust_id=get_id(uname,pw,role)
        c= Customer(cust_id,uname,pw,role)
        while True:
            try:
                choice=int(input("\nPress keys to proceed:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Check Account Details\n5. Exit\nEnter your choice:"))
                match choice:
                    case 1:
                        c.deposit_amt()
                    case 2:
                        c.withdraw_amt()
                    case 3:
                        c.check_balance()
                    case 4:
                        c.check_acc_details()
                    case 5:
                        print("You've been logged out.")
                        break
                    case _:
                        print("Please a valid choice.")                      
            except ValueError:
                print("Please enter a valid choice.")
else:
    print("Invalid username or password!")