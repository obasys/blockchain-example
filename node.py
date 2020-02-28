from blockchain import Blockchain
from wallet import Wallet

from utils.verification import Verification

class Node:

    def __init__(self):
        # self.id = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    def get_transaction_data(self):
        # sender = input("Input new transaction sender: ")
        recipient = input("Input new transaction recipient: ")
        amount = float(input("Input new transaction amount: "))

        return (recipient, amount)

    def get_user_choice(self):
        return input("Input your choice: ")

    def display_blockchain(self):
        for block in self.blockchain.get_chain():
            print('Outputting Block')
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):

        wait_for_input = True

        while wait_for_input:
            print("Choose action: ")
            print("1. Add new element into the blockchain")
            print("2. Mine new block")
            print("3. Print blockchain")
            # print("4. Print participants")
            print("4. Check transactions validity")
            print("5. Create wallet")
            print("6. Load wallet")
            print("7. Save wallet keys")
            # print("h: Manipulate blockchain")
            print("q. Quit")

            action = self.get_user_choice()

            if action == '1':
                transaction_data = self.get_transaction_data()
                recipient, amount = transaction_data

                signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)

                if self.blockchain.add_transaction(self.wallet.public_key, recipient, amount, signature):
                    print("Added transaction!")
                else:
                    print("Transcation failed!")

                print(self.blockchain.get_open_transactions())

            elif action == '2':
                if not self.blockchain.mine_block():
                    print("Mining failed. Got no wallet.")

            elif action == '3':
                self.display_blockchain()

            # elif action == '4':
            #     print("Participants: ", participants)

            elif action == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")

            elif action == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)

            elif action == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)

            elif action == '7':
                self.wallet.save_keys()

            # elif action == 'h':
            #
            #     if len(blockchain) >= 1:
            #         blockchain[0] = {
            #             'previous_hash': "",
            #             'index': 0,
            #             'transactions': [{'sender': 'Tim', 'recipient': 'Steve', 'amount': 10}]
            #         }

            elif action == 'q':
                break

            else:
                print("Invalid input! Please input correct")

            if not Verification.verify_blockchain(self.blockchain.get_chain()):
                self.display_blockchain()
                print("Blockchain is invalid")
                break

            print("Balance of {}: {:.2f}".format(self.wallet.public_key, self.blockchain.get_balance()))

        print("Done!")

node = Node()

node.listen_for_input()