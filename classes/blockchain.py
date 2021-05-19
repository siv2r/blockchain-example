from classes.block import Block
from classes.transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenisisBlock()]
        self.difficulty = 2
        self.remainingTransactions = []

    def createGenisisBlock(self):
        """Create the first block (genisis) for the blockchain block

        Returns:
            Block: Returns the genisis block
        """
        return Block([Transaction()], "0000")

    def getLastBlock(self):
        """Returns the last block in the blockchain

        Returns:
            Block: final block in the chain
        """
        return self.chain[-1]

    def mineRemainingTransactions(self):
        """Adds all the transaction present in the transaction queue of a blockchain to this block
        """
        block = Block(self.remainingTransactions)
        block.mineBlock(self.difficulty)
        self.chain.append(block)
        print("New block added : {}".format(block.hash))

    def addTransactions(self, transaction):
        """adds the new transaction to the transaction queue in the blockchain

        Args:
            transaction (Transaction): the new transaction

        Raises:
            Exception: If the transaction does not have a valid signature
        """
        if transaction.isValid() == False:
            raise Exception("The transaction is not valid")
        self.remainingTransactions.append(transaction)

    def getBalanceOfNode(self, node, asset):
        """Retruns the wallet balance of a node

        Args:
            node (fastecdsa.point): The node representation
            asset (str): The assest that we need the balance for

        Returns:
            int: The quantity of assest that this current node has
        """
        balance = 0

        for block in self.chain:
            for trans in block.transactions:
                if repr(trans.source) == repr(node) and trans.asset == asset:
                    balance -= trans.quantity

                elif repr(trans.destination) == repr(node) and trans.asset == asset:
                    balance += trans.quantity

        return balance

    def isValidChain(self):
        """Checks the itegrity of blockchain

        Returns:
            bool: return True/False according the validity of te blockchain
        """
        for i in range(1, len(self.chain)):
            currBlock = self.chain[i]
            prevBlock = self.chain[i - 1]

            if currBlock.hasValidTransactions() == False:
                return False

            # check if data of the current block was changed
            if currBlock.hash != currBlock.calcHash():
                return False

            if currBlock.prevHash != prevBlock.hash:
                return False

        return True

    def displayChain(self):
        """Prints the content of the block chain to the terminal
        """
        for i in range(len(self.chain)):
            print("--------Block {}-------".format(i + 1))
            block = self.chain[i]
            for j in range(len(block.transactions)):
                tran = block.transactions[j]
                print("--Transaction {}:".format(j))
                print(
                    "Source = {}, Destination = {}, Asset = {}, Quantity = {}".format(
                        repr(tran.source),
                        repr(tran.destination),
                        tran.asset,
                        tran.quantity,
                    )
                )
