import hashlib
import json
from datetime import datetime


class Block:
    def __init__(
        self,
        transactions,
        prevHash="",
        hash="",
        nonce=0,
        timestamp=datetime.now().timestamp(),
    ):
        """Consturctor of a Block

        Args:
            transactions (Transaction): List of all transaction in the Block
            prevHash (str, optional): Hasf of the previous block. Defaults to "".
            hash (str, optional): Hash of the this block. Defaults to "".
            nonce (int, optional): nonce value for proof of work algorithm. Defaults to 0.
            timestamp ([type], optional): Time when a block is created. Defaults to datetime.now().timestamp().
        """        
        self.transactions = transactions
        self.timestamp = timestamp
        self.prevHash = prevHash
        self.hash = hash
        self.nonce = nonce

    def calcHash(self):
        """Calculates the hash valus of the Block

        Returns:
            str: return the hash value
        """        
        toBeHashed = "".join(
            [
                str(self.transactions),
                str(self.prevHash),
                str(self.nonce),
                str(self.timestamp),
            ]
        )

        return str(hashlib.sha256(toBeHashed.encode()).hexdigest())

    def mineBlock(self, difficulty):
        """Restricts the hash value pattern (Proof for work to)

        Args:
            difficulty (int): sets difficulty for computing the hash value
        """        
        while self.hash[0:difficulty] != "".join(["0"] * difficulty):
            self.nonce += 1
            self.hash = self.calcHash()

    def hasValidTransactions(self):
        """Checks the validity of transactions in a block.

        Returns:
            bool: returns a True/False according to the validity
        """
        for tran in self.transactions:
            if tran.isValid() == False:
                return False

        return True
