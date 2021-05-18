from classes.block import Block


class Blockchain:
    def __init__(self):
        self.chain = list()
        self.chain.append(self.createGenisisBlock())
        self.difficulty = 2

    def createGenisisBlock(self):
        """Creates the starting block for the blockchain

        Returns:
                Block: starting block with 0000 as hash value
        """
        return Block(0, {"Name": "Genisis Block", "Balance": "1000"}, "00000")

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
        newBlock.hash = newBlock.mineBlock(self.difficulty)
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
