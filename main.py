from block import Block  


class server():
    def __init__(self, hostname, public_ip_addr):
        self.__hostname = hostname
        self._public_ip_addr = public_ip_addr
        self.genesisBlock = Block("The Genesis Block of Alpoe",'Transactions example')
    
    def addBlock(self, transaction, prev_hash):
        pass

    def createTransaction(phase, status, value, quantity):
        {
            'Production Stage' : phase,
            'Status' : status,
            'Value/ Quantity' : quantity,
            'Time' : '3 Mar 2021 11:45:34 GMT'
        }



## Genesis Block - First Block in the Blockchain
genesisBlock = Block("The Genesis Block of Alpoe",'Transactions example')

secondBlock = Block(genesisBlock.block_hash, 'Transactions')
print (genesisBlock.block_hash)