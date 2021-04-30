from customClass.blockchain import Block
from customClass.blockchain import Blockchain

# Defining main function 
def main(): 

    # newBlock = list()
    # newBlock.append(Block(0, {"Name": "Genisis Block", "Balance": "1000"}, "0000"))
    # print(newBlock)


    accBalances = Blockchain()
    accBalances.addNewBlock(Block(1, {"name":"Sivaram", "Balance":"10000000"}))
    accBalances.addNewBlock(Block(2, {"name":"randomDude1", "Balance":"10000"}))
    accBalances.addNewBlock(Block(3, {"name":"randomDude2", "Balance":"100000"}))

    print("Is the chain valid? {}".format(accBalances.isValidChain()))

    #randomDude1 is trying to manipulate his acc balance
    accBalances.chain[1].data = {"name":"randomDude1", "Balance":"10000"}
    accBalances.chain[1].hash = accBalances.chain[1].calcHash

    #check if the chain is valid
    print("Is the chain valid? {}".format(accBalances.isValidChain()))

  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 