from web3 import Web3

ganeche_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganeche_url))
from_account = '0xE89dc8FFD6e0D262F67239Cef70787951EC8B1CB'
to_account = '0x46B78eA3C0e04fa92Ab84C6f6588979786a67ee8'
from_private_key = '2a53233dbf3416cc56d80e3ba44d2782202cbf65051c3acfdee159dabfd48949'

# get the nonce
nonce = web3.eth.getTransactionCount(from_account)
# build taransaction
tx = {
'nonce': nonce,
'to': to_account,
'value': web3.toWei(1, 'ether'),
'gas': 200000, # 0.2m
'gasPrice': web3.toWei(50, 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, from_private_key)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(web3.toHex(tx_hash))