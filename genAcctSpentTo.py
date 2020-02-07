import params
from algosdk import account, encoding, mnemonic, algod, transaction

# create an algod client
acl = algod.AlgodClient(params.algod_token, params.algod_address)

# generate an account
private_key, address = account.generate_account()
# extract the mnemonic phrase from the private key
mn = mnemonic.from_private_key(private_key)
print("Private key:", private_key)
print("Mnemonic:", mn)
print("Address:", address)

# input("Please go to: https://bank.testnet.algorand.network/ to fund your account." + '\n' + "Press Enter to continue...")

# check if the address is valid
if encoding.is_valid_address(address):
    print("The address is valid!")
else:
    print("The address is invalid.")

# get suggested parameters
params = acl.suggested_params()
gen = params["genesisID"]
gh = params["genesishashb64"]
last_round = params["lastRound"]
fee = params["fee"]

# create a transaction
receiver = "PLBXE3DQD6X6GL7GC3RCUUT6X5HKOVEN6LBSZR7YACJDKV53A4U2IGR7VE"
amount = 10000
txn = transaction.PaymentTxn(address, fee, last_round, last_round+100, gh, receiver, amount)

# sign transaction
signed_txn = txn.sign(private_key)

# send transaction to the network
txn_id = acl.send_transaction(signed_txn)
print("\nTransaction was sent!")
print("Transaction ID: " + txn_id + "\n")
