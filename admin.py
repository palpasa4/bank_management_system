from user import Customer
from bank_acc import BankAccount
import json,uuid
from data import load_json,write_json,to_dict

class Admin(Customer):

    def __init__(self, cust_id: str, username: str, password: str, role: str):
        super().__init__(cust_id, username, password, role)

    #create a relation: cust_id->bank_acc_id 
    def create_relation(self,cust_id:str,bank_acc_id:str):
        data=load_json("database/relation.json")
        new_relation={
            "cust_id":cust_id,
            "bank_acc_id":bank_acc_id
        }  
        data.append(new_relation) 
        write_json("database/relation.json",data)  

    def create_user(self)->None:
        print("\nEnter login details for the user:")
        new_uname=input("Enter username: ")
        new_pw=input("Enter password: ")
        data=load_json("database/user_data.json")
        if (any(user for user in data if user["username"] == new_uname)):
            print("Error creating user. Enter details again.")
            self.create_user()
        else:
            cust_id=f"CUST-{str(uuid.uuid4())[:8]}"
            c=Customer(cust_id,new_uname,new_pw,"user")
            new_data=to_dict(c)
            data.append(new_data)
            write_json("database/user_data.json",data)            
            print("\nEnter bank account details of the user:")
            fullname=input("Full Name: ")
            address=input("Address: ")
            contact_no=input("Contact Number: ")
            while True:
                balance=float(input("Opening Deposit Amount [Minimum deposit: 500]: "))
                if(balance<500):
                    print("*Minimum opening balance is 500! Enter amount again.\n")
                else:
                    bank_acc_id= f"ACC-{str(uuid.uuid4())[:8]}"
                    new_user={
                        "bank_acc_id":bank_acc_id,
                        "fullname": fullname,
                        "address": address,
                        "contact_no": contact_no,
                        "balance": balance
                    }  
                    data=load_json("database/bank_acc.json") 
                    data.append(new_user)
                    write_json("database/bank_acc.json",data)
                    print(f"Bank account successfully create for '{new_uname}' with Customer ID: {cust_id}")
                    break  
            self.create_relation(cust_id,bank_acc_id)  

    def view_users(self):
        users=load_json("database/user_data.json")
        i=1
        for user in users:
            if(user["username"]!="admin"):
                print(f"Customer {i}\nCustomer ID: {user["cust_id"]}\nUsername: {user["username"]}\n")
                i+=1