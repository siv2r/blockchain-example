class Block:
  def __init__(self, index, data, previousHash):
    self.index = index
    self.data = data
    self.previousHash = previousHash
  def myfunc(self):
    print("Hello my name is " + self.name +".")