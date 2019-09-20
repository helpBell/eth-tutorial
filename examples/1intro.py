from web3 import Web3

ganeche_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganeche_url))
print(web3.isConnected()) #True

print(web3.eth.blockNumber) #0

balance = web3.eth.getBalance('0x46B78eA3C0e04fa92Ab84C6f6588979786a67ee8')
print(balance) #10000~

ether = web3.fromWei(balance, 'ether')
print(ether) #100(ether)