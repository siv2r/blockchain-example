from classes.block import Block
from classes.transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenisisBlock()]  # check this
        self.difficulty = 2
        self.remainingTransactions = []

    def createGenisisBlock(self):
        """Creates the starting block for the blockchain

        Returns:
                Block: starting block with 0000 as hash value
        """
        return Block([Transaction()], "0000")

    def getLastBlock(self):
        """Returns the last block of the chain

        Returns:
                Block: The last block of the chain
        """
        return self.chain[-1]

    def mineRemainingTransactions(self):
        block = Block(self.remainingTransactions)
        block.mineBlock(self.difficulty)
        self.chain.append(block)
        print("New block added : {}".format(block.hash))

    def createTransactions(self, transaction):
        self.remainingTransactions.append(transaction)

    def getBalanceOfNode(self, node, asset):
        balance = 0

        for block in self.chain:
            for trans in block.transactions:
                if trans.source == node and trans.asset == asset:
                    balance -= trans.quantity

                elif trans.destination == node and trans.asset == asset:
                    balance += trans.quantity

        return balance

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

    def displayChain(self):
        for i in range(len(self.chain)):
            print("--------Block {}-------".format(i + 1))
            block = self.chain[i]
            for j in range(len(block.transactions)):
                tran = block.transactions[j]
                print("--Transaction {}:".format(j))
                print(
                    "Source = {}, Destination = {}, Asset = {}, Quantity = {}".format(
                        tran.source, tran.destination, tran.asset, tran.quantity
                    )
                )
