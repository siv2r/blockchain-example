from classes.block import Block
from classes.blockchain import Blockchain
from classes.transaction import Transaction


def main():
    dlt = Blockchain()
    dlt.createTransactions(Transaction("node1", "node2", "pencil", 100))
    dlt.createTransactions(Transaction("node2", "node1", "pencil", 20))

    print("Registering transactions to blockchain.....")
    dlt.mineRemainingTransactions()

    print(dlt.getBalanceOfNode("node2", "pencil"))


if __name__ == "__main__":
    main()
