import hashlib
from fastecdsa import keys, curve, ecdsa


class Transaction:
    def __init__(self, source=None, destination=None, asset=None, quantity=None):
        """Constructor

        Args:
            source (fastecdsa.point, optional): The sender for the transaction. Defaults to None.
            destination (fastecdsa.point, optional): Reciever for the transactions. Defaults to None.
            asset (str, optional): The asset that is tranfered. Defaults to None.
            quantity (int, optional): The amount of asset that is tranfered. Defaults to None.
        """
        self.source = source
        self.destination = destination
        self.asset = asset
        self.quantity = quantity
        self.signature = None

    def calcHash(self):
        """Caculates the hash for the transactions

        Returns:
            str: Return the hash value
        """
        toBeHashed = "".join(
            [
                str(self.source),
                str(self.destination),
                str(self.asset),
                str(self.quantity),
            ]
        )

        return str(hashlib.sha256(toBeHashed.encode()).hexdigest())

    def signTransaction(self, signingKeys):
        """Signs the transaction to check the authenticity of the sender and

        Args:
            signingKeys (fastecdsa.point): The public, private key pair of the sender

        Raises:
            Exception: If a node tries to transfer the asset of another node
        """
        privateKey, publicKey = signingKeys
        if publicKey != self.source:
            raise Exception("You cannot sign transaction for other nodes")

        transactionHash = self.calcHash()
        self.signature = ecdsa.sign(transactionHash, privateKey)

    def isValid(self):
        """Validity of the transactions 

        Raises:
            Exception: If a transaction is left unsigned or

        Returns:
            bool: return True/False wrt to the validity of the node
        """
        if repr(self.source) == repr(None):
            return True

        if self.signature == None:
            raise Exception("No signature in this transaction")

        return ecdsa.verify(self.signature, self.calcHash(), self.source)
