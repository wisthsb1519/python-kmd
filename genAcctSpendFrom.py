import params
from algosdk import account, encoding, mnemonic, algod, transaction

# create an algod client
acl = algod.AlgodClient(params.algod_token, params.algod_address)

# generate an sender account
sender_private_key, sender = account.generate_account()
# extract the mnemonic phrase from the private key
sender_mn = mnemonic.from_private_key(sender_private_key)
print("Sender Private key:", sender_private_key)
print("Sender Mnemonic:", sender_mn)
print("Sender Address:", sender)
# check if the address is valid
if encoding.is_valid_address(sender):
    print("The address is valid!" + '\n')
else:
    print("The address is invalid." + '\n')

input("Please go to: https://bank.testnet.algorand.network/ to fund your sender address." + '\n' + "Press Enter to continue..." + '\n')

# generate an receiver account
receiver_private_key, receiver = account.generate_account()
# extract the mnemonic phrase from the private key
receiver_mn = mnemonic.from_private_key(receiver_private_key)
print("Receiver Private key:", receiver_private_key)
print("Receiver Mnemonic:", receiver_mn)
print("Receiver Address:", receiver)

# check if the address is valid
if encoding.is_valid_address(receiver):
    print("The address is valid!"+ '\n')
else:
    print("The address is invalid." '\n')

input("Please go to: https://bank.testnet.algorand.network/ to fund your receiver address." + '\n' + "Press Enter to continue..."'\n')

# get suggested parameters
params = acl.suggested_params()
gen = params["genesisID"]
gh = params["genesishashb64"]
last_round = params["lastRound"]
fee = params["fee"]

# create a transaction
receiver = "PLBXE3DQD6X6GL7GC3RCUUT6X5HKOVEN6LBSZR7YACJDKV53A4U2IGR7VE"
amount = 10000
txn = transaction.PaymentTxn(sender, fee, last_round, last_round+100, gh, receiver, amount)

# sign transaction
signed_txn = txn.sign(sender_private_key)

# send transaction to the network
txn_id = acl.send_transaction(signed_txn)
print("\nTransaction was sent!")
print("Transaction ID: " + txn_id + "\n")
