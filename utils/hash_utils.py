import hashlib
import json

def hash_string(string):
    return hashlib.sha256(string).hexdigest()

def hash_block(block):
    hashable_block = block.__dict__.copy()

    hashable_block['transactions'] = [transaction.to_ordered_dict() for transaction in hashable_block['transactions']]

    return hash_string(json.dumps(hashable_block, sort_keys=True).encode())
    # return '-'.join([str(block[key]) for key in block])
