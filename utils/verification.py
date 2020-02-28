from utils.hash_utils import hash_string, hash_block
from wallet import Wallet

class Verification:

    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        guess = (str([transaction.to_ordered_dict() for transaction in transactions]) + str(last_hash) + str(proof)).encode()
        guess_hash = hash_string(guess)

        # print("Proof:", proof, "Hash guess:", guess_hash)

        return guess_hash[:2] == '00'

    @classmethod
    def verify_blockchain(cls, blockchain):
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue

            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False

            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print("Invalid proof of work")
                return False

        return True

    @classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        return all([cls.verify_transaction(transaction, get_balance) for transaction in open_transactions])

    @staticmethod
    def verify_transaction(transaction, get_balance, checkFunds=True):

        if checkFunds == True:
            sender_balance = get_balance()
            return transaction.amount > 0 and sender_balance >= transaction.amount and Wallet.verify_transaction(transaction)

        return Wallet.verify_transaction(transaction)

