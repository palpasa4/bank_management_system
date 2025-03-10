from data import load_json, write_json

class BankAccount:
    def __init__(self,bank_id:str) -> None:
        self.bank_id=bank_id

    def deposit(self,new_balance:float)->bool:
        accounts=load_json("database/bank_acc.json")
        for account in accounts:
            if(account["bank_acc_id"]==self.bank_id):
                account["balance"]=new_balance
        write_json("database/bank_acc.json",accounts)
        return True

    def withdraw(self,new_balance:float)->bool:
        accounts=load_json("database/bank_acc.json")
        for account in accounts:
            if(account["bank_acc_id"]==self.bank_id):
                account["balance"]=new_balance
        write_json("database/bank_acc.json",accounts)
        return True

    def get_balance(self)->float:
        accounts=load_json("database/bank_acc.json")
        for account in accounts:
            if(self.bank_id==account["bank_acc_id"]):
                break
        return float(account["balance"])
    
    def get_fullname(self)->str:
        accounts=load_json("database/bank_acc.json")
        for account in accounts:
            if(self.bank_id==account["bank_acc_id"]):
                break
        return account["fullname"]

    def get_details(self)->None:
        accounts=load_json("database/bank_acc.json")
        for account in accounts:
            if(self.bank_id==account["bank_acc_id"]):
                print("Your bank account details:\n")
                print(f"Bank Account No: {self.bank_id}")
                print(f"Full Name: {account["fullname"]}")
                print(f"Address: {account["address"]}")
                print(f"Contact No: {account["contact_no"]}")
                print(f"Balance: {account["balance"]}")