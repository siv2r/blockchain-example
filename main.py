from customClass.blockchain import Block
from customClass.blockchain import Blockchain

# Defining main function 
def main(): 

    # newBlock = list()
    # newBlock.append(Block(0, {"Name": "Genisis Block", "Balance": "1000"}, "0000"))
    # print(newBlock)


    bankBalances = Blockchain()
    bankBalances.addNewBlock(Block(1, {"name":"Sivaram", "Balance":"10000000"}))
    bankBalances.addNewBlock(Block(2, {"name":"randomDude1", "Balance":"10000"}))
    bankBalances.addNewBlock(Block(3, {"name":"randomDude2", "Balance":"100000"}))

    print("Is the chain valid? {}".format(bankBalances.isValidChain()))

    #randomDude1 is trying to manipulate his bank balance
    bankBalances.chain[1].data = {"name":"randomDude1", "Balance":"10000"}
    bankBalances.chain[1].hash = bankBalances.chain[1].calcHash

    #check if the chain is valid
    print("Is the chain valid? {}".format(bankBalances.isValidChain()))

  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 