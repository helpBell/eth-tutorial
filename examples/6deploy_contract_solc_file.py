import os
from web3 import Web3
from solcx import compile_files

dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
greeter_path = os.path.join(dir_path, 'Greeter.sol')
# print(greeter_path)
compiled_greeter = compile_files([greeter_path])
greeter_key = greeter_path + ':Greeter'
greeter_abi = compiled_greeter[greeter_key]['abi']
greeter_bytecode = compiled_greeter[greeter_key]['bin']

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

Greeter = web3.eth.contract(abi = greeter_abi, bytecode = greeter_bytecode)
tx_hash = Greeter.constructor().transact()
tx_recipt = web3.eth.waitForTransactionRecipt(tx_hash)

greeter = web3.eth.contract(address = tx_recipt.contractAddress, abi = greeter_abi)
print(greeter.functions.greet().call())
tx_hash = greeter.functions.setGreeting('hello').transact()
tx_recipt = web3.eth.waitForTransactionRecipt(tx_hash)
print(greeter.functions.greet().call())