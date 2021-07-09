import hashlib
import string
import random
from .Block import Block
from .Wallet import Wallet
import sys
from datetime import datetime


class Chain:
    def init(self):
        self.blocks = []
        self.last_transaction_number = 0

    def generate_hash(self):
        block = Block()
        block.hash = hashlib.sha256(string.encode('utf-8')).hexdigest()


    def verify_hash(self, hash_to_verify):
        if not hash_to_verify.startswith("0"):
            return False

        for b in self.blocks:
            if b.hash == hash_to_verify:
                return False

        return True

    def add_block(self, random_string, new_hash):
        if len(self.blocks) < 1:
            parent_hash = "00"
        else:
            parent_hash = self.blocks[len(self.blocks) - 1].hash

        block = Block(random_string, new_hash, parent_hash)
        if block is not False:
            block.save()
            self.blocks.append(block)
            return True
        else:
            return False

    def get_block(self, block_hash):
        for b in self.blocks:
            if b.hash == block_hash:
                return b

        return None

    def add_transaction(self, emitter_uuid, receiver_uuid, amount):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        emitter = Wallet(emitter_uuid)
        if emitter is not False:
            if emitter.balance >= amount:
                receiver = Wallet(receiver_uuid)
                if receiver is not False:
                    last_block = self.blocks[len(self.blocks) - 1]

                    transaction = {
                        'number': self.last_transaction_number + 1,
                        'emitter': emitter_uuid,
                        'receiver': receiver_uuid,
                        'amount': amount,
                        'date': date
                    }
                    if sys.getsizeof(transaction) + last_block.get_weight() <= 256000:
                        result = last_block.add_transaction(transaction)
                        if result is not True:
                            return "Something wrong happened, try again later."
                        else:
                            emitter.sub_balance(transaction)
                            receiver.add_balance(transaction)
                            self.last_transaction_number += 1
                            return True
                    else:
                        return "Receiver doesn't exist."
            else:
                return "emitter doesn't have enough balance for this transaction."

    def find_transaction(self, number):
            for b in self.blocks:
                if b.get_transaction(number) is not None:
                    return b



