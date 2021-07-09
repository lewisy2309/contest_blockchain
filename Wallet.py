import uuid
import json

class Wallet:
    unique_id= ""
    balance=0
    history=[]

    def __init__(self):
        self.unique_id=self.generate_unique_id()

    def add_balance(self, fund):
        self.balance+=fund
        return self.balance

    def sub_balance(self, fund):
        if self.balance>=fund:
            self.balance-=fund

        else:
            print("opération impossible votre solde de "+str(self.balance)+" est inférieur à "+ str(fund))
        return self.balance

    def generate_unique_id(self):

        self.unique_id=uuid.uuid4()
        return self.unique_id

    def send(self):
        pass

    def save(self):
        with open("./content/wallets/{}.json".format(self.unique_id), "x") as file:
            file.write(json.dumps({"unique_id": str(self.unique_id), "balance": self.balance, "history": self.history}))

    def load(self, id_wallet):
        file='./content/wallets/'+id_wallet+'.json'
        with open(file,'r') as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
            self.unique_id=jsonObject['unique_id']
            self.balance=jsonObject['balance']
            self.history=jsonObject['history']

a=Wallet()
a.save()

