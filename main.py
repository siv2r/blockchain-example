from classes.block import Block
from classes.blockchain import Blockchain
from classes.transaction import Transaction
from fastecdsa import keys, curve, ecdsa

def main():

    node1Key, node1Address = keys.gen_keypair(curve.P256) 
    node2Key, node2Address = keys.gen_keypair(curve.P256) 

    dlt = Blockchain()

    tx1 = Transaction(None, node1Address, 'sheep', 50)
    dlt.addTransactions(tx1)

    tx2 = Transaction(node1Address, node2Address, 'sheep', 10)
    tx2.signTransaction((node1Key, node1Address))
    dlt.addTransactions(tx2)

    print("Registering transactions to blockchain.....")
    dlt.mineRemainingTransactions()

    print(dlt.getBalanceOfNode(node1Address, "sheep"))
    print(dlt.getBalanceOfNode(node2Address, "sheep"))
    print(dlt.displayChain())


if __name__ == "__main__":
    main()
