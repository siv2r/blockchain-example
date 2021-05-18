import hashlib
import json
from datetime import datetime


class Block:
    def __init__(self, index, data, prevHash=""):
        """Constructor for the Block class

        Args:
                index (int): To mark the position of the block in the chain
                data (dict): Data that each block stores (here, bank acc details)
                prevHash (string): Hash of the prev block. 0000 for Genisis block
        """
        self.index = index
        self.timestamp = datetime.now().timestamp()
        self.data = data.copy()
        self.prevHash = prevHash
        self.hash = ""
        self.nonce = 0

    def calcHash(self):
        """Function to caculate hash value for a block

        Returns:
                string: Hash value of a block
        """
        toBeHashed = "".join(
            [
                str(self.index),
                str(json.dumps(self.data)),
                str(self.prevHash),
                str(self.nonce),
                str(self.timestamp),
            ]
        )

        return str(hashlib.sha256(toBeHashed.encode()).hexdigest())

    def mineBlock(self, difficulty):
        while self.hash[0:difficulty] != "".join(["0"] * difficulty):
            self.nonce += 1
            self.hash = self.calcHash()

        print("New block added: {}".format(self.hash))
