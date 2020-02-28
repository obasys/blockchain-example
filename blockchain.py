import functools
import json

from block import Block
from transaction import Transaction
from wallet import Wallet

from utils.hash_utils import hash_block
from utils.verification import Verification

MINING_REWARD = 10

class Blockchain:

    def __init__(self, hosting_node_id):
        GENESIS_BLOCK = Block(0, "", [], 100, 0)
        self.__chain = [GENESIS_BLOCK]
        self.__open_transactions = []
        self.hosting_node = hosting_node_id
        self.fetch_data()

    def get_chain(self):
        return self.__chain[:]

    def get_open_transactions(self):
        return self.__open_transactions[:]

    def save_data(self):
        try:
            with open('blockchain.txt', mode='w') as file:
                saveable_blockchain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]]

                file.write(json.dumps(saveable_blockchain))
                file.write('\n')

                saveable_transaction = [transaction.__dict__ for transaction in self.__open_transactions]

                file.write(json.dumps(saveable_transaction))
        except (IOError, IndexError):
            print("Saving failed!")

    def fetch_data(self):

        try:
            with open('blockchain.txt', mode='r') as file:
                file_content = file.readlines()
                self.__chain = json.loads(file_content[0][:-1])

                updated_blockchain = []

                for block in self.__chain:
                    converted_transactions = [Transaction(transaction['sender'], transaction['recipient'], transaction['amount'], transaction['signature']) for transaction in block['transactions']]

                    fetched_block = Block(block['index'], block['previous_hash'], converted_transactions, block['proof'], block['timestamp'])

                    updated_blockchain.append(fetched_block)

                self.__chain = updated_blockchain

                open_transactions = json.loads(file_content[1])

                updated_transactions = []

                for transaction in open_transactions:
                    fetched_transaction = Transaction(transaction['sender'], transaction['recipient'], transaction['amount'], transaction['signature'])

                    updated_transactions.append(fetched_transaction)

                open_transactions = updated_transactions

        except (IOError, IndexError):
           print("Handled error...")
        finally:
            print("Cleanup!")

    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)

        proof = 0

        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1

        return proof

    def get_balance(self):

        participant = self.hosting_node

        tx_sender = [[transaction.amount for transaction in block.transactions if transaction.sender == participant] for block in self.__chain]

        open_tx_sender = [transaction.amount for transaction in self.__open_transactions if transaction.sender == participant]

        tx_sender.append(open_tx_sender)

        amount_sent = functools.reduce(
            lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_sender, 0)

        # amount_sent = 0
        #
        # for tx in tx_sender:
        #     if len(tx) > 0:
        #         amount_sent += tx[0]

        tx_recipient = [[transaction.amount for transaction in block.transactions if transaction.recipient == participant] for block in self.__chain]

        amount_received = functools.reduce(
            lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum + 0, tx_recipient, 0)

        # amount_received = 0
        #
        # for tx in tx_recipient:
        #     if len(tx) > 0:
        #         amount_received += tx[0]

        return amount_received - amount_sent

    def get_last_blockchain_transaction(self):
        if len(self.__chain) < 1:
            return None

        return self.__chain[-1]

    def add_transaction(self, sender, recipient, amount, signature):

        if self.hosting_node == None:
            return False

        transaction = Transaction(sender, recipient, amount, signature)

        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)

            # participants.add(sender)
            # participants.add(recipient)

            self.save_data()

            return True

        return False

    def mine_block(self):

        if self.hosting_node == None:
            return False

        hashed_block = hash_block(self.__chain[-1])

        print("Hashed blocks result:" , hashed_block)

        proof = self.proof_of_work()

        reward_transaction = Transaction('Miner', self.hosting_node, MINING_REWARD, '')

        copied_transactions = self.__open_transactions[:]

        for transaction in copied_transactions:
            if not Wallet.verify_transaction(transaction):
                return False

        copied_transactions.append(reward_transaction)

        block = Block(len(self.__chain), hashed_block, copied_transactions, proof)

        self.__chain.append(block)

        self.open_transactions = []
        self.save_data()

        return True

# def verify_blockchain():
#     # block_index = 0
#     is_valid = True
#
#     for block_index in range(len(blockchain)):
#         if block_index == 0:
#             continue
#         elif blockchain[block_index][0] == blockchain[block_index - 1]:
#             is_valid = True
#         else:
#             is_valid = False
#             break
#     # for block in blockchain:
#     #     if block_index == 0:
#     #         block_index += 1
#     #         continue
#     #     elif block[0] == blockchain[block_index - 1]:
#     #         is_valid = True
#     #     else:
#     #         is_valid = False
#     #         break
#     #
#     #     block_index += 1
#
#     return is_valid
