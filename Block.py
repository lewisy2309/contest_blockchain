import hashlib
import json
from pathlib import Path


class Block:
    base_hash = 256
    hash = ""
    parent_hash = ""
    transaction = []

    def __init__(self):
        pass

    def __init__(self, string):
        self.hash = hashlib.sha256(string.encode('utf-8')).hexdigest()

    def __init__(self, base_hash ,hash,parent_hash):
        self.hash=hash
        self.base_hash=base_hash
        self.parent_hash=parent_hash


    def check_ash(self):
        pass

    def add_transaction(self,sender_wallet,receiver_wallet,amount):
        transaction_infos={"sender_wallet":str(sender_wallet),"receiver_wallet":str(receiver_wallet),"amount":amount}
        self.transaction.append(transaction_infos)
        return self.transaction

    def get_transaction(self, index):
        if not self.transaction:
            if index>=0 and index<=len(self.transaction):
                return self.transaction[index]
            else:
                return 'Cannot reach the transaction'
        else:
            return print('No transaction available for thi block')

    def get_weight(self, hash):
        block = './content/wallets/' + hash + '.json'
        weight=Path(block).stat().st_size
        return weight


    def save(self):
        with open("./content/blocks/{}.json".format(self.hash), "x") as file:
            file.write(json.dumps({"hash": str(self.hash), "parent_hash": self.parent_hash, "base_hash": self.base_hash,"transaction":self.transaction}))

    def load(self, hash):
        file = './content/blocks/' + hash + '.json'
        with open(file, 'r') as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
            self.hash = jsonObject['hash']
            self.parent_hash = jsonObject['parent_hash']
            self.base_hash = jsonObject['base_hash']
            self.transaction = jsonObject['tansaction']
a=Block('a')

print(a.hash)


