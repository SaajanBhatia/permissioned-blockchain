from block import Block  

blockchain = []

## Genesis Block - First Block in the Blockchain
genesisBlock = Block("The Genesis Block of Alpoe",'Transactions example')

secondBlock = Block(genesisBlock.block_hash, 'Transactions')
print (genesisBlock.block_hash)