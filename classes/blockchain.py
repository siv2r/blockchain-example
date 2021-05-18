import hashlib
import json


class Block:
    def __init__(self, index, data, prevHash=" "):
        """Constructor for the Block class

        Args:
                index (int): To mark the position of the block in the chain
                data (dict): Data that each block stores (here, bank acc details)
                prevHash (string): Hash of the prev block. 0000 for Genisis block
        """
        self.index = index
        self.data = data.copy()
        self.prevHash = prevHash
        self.hash = ""

    def calcHash(self):
        """Function to caculate hash value for a block

        Returns:
                string: Hash value of a block
        """
        toBeHashed = str(self.index) + json.dumps(self.data) + self.prevHash
        return str(hashlib.sha256(toBeHashed.encode()).hexdigest())


class Blockchain:
    def __init__(self):
        self.chain = list()
        self.chain.append(self.createGenisisBlock())

    def createGenisisBlock(self):
        """Creates the starting block for the blockchain

        Returns:
                Block: starting block with 0000 as hash value
        """
        return Block(0, {"Name": "Genisis Block", "Balance": "1000"}, "0000")

    def getLastBlock(self):
        """Returns the last block of the chain

        Returns:
                Block: The last block of the chain
        """
        return self.chain[-1]

    def addNewBlock(self, newBlock):
        """Adds new block to the chain

        Args:
                newBlock (Block): Value of the block to add to the chain
        """
        newBlock.prevHash = self.getLastBlock().hash
        newBlock.hash = newBlock.calcHash()
        self.chain.append(newBlock)

    def isValidChain(self):
        """Checks if a block chain is valid or not. i.e, if anyone manipulated the data

        Returns:
                [type]: [description]
        """
        for i in range(1, len(self.chain)):
            currBlock = self.chain[i]
            prevBlock = self.chain[i - 1]

            # check if data of the current block was changed
            if currBlock.hash != currBlock.calcHash():
                return False

            if currBlock.prevHash != prevBlock.hash:
                return False

        return True
