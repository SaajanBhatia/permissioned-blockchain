import hashlib

class Block(object):
    def __init__(self, prev_hash, transactions):
        self.prev_hash = prev_hash
        self.transactions = transactions
        initial = "".join(transactions) + prev_hash
        self.block_hash = hashlib.sha256(initial.encode()).hexdigest()