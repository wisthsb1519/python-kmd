import params
from algosdk import account, transaction, algod, encoding

acl = algod.AlgodClient(params.algod_token, params.algod_address)

# generate three accounts
private_key_1, account_1 = account.generate_account()
private_key_2, account_2 = account.generate_account()
private_key_3, account_3 = account.generate_account()
print("Account 1:", account_1)
print("Account 2", account_2)
print("Account 3:", account_3)

# create a multisig account
version = 1  # multisig version
threshold = 2  # how many signatures are necessary
msig = transaction.Multisig(version, threshold, [account_1, account_2])
print(msig.address())
input("Please go to: https://bank.testnet.algorand.network/ to fund your multisig account." + '\n' + "Press Enter to continue...")

# get suggested parameters
params = acl.suggested_params()
gen = params["genesisID"]
gh = params["genesishashb64"]
last_round = params["lastRound"]
fee = params["fee"]

# create a transaction
sender = msig.address()
amount = 10000
txn = transaction.PaymentTxn(sender, fee, last_round, last_round+100, gh, account_3, amount)

# create a SignedTransaction object
mtx = transaction.MultisigTransaction(txn, msig)

# sign and append the transaction
# see for details https://github.com/algorand/py-algorand-sdk/blob/b079db660ae92d0dbf24dc04f28eb722711e426f/algosdk/transaction.py#L862
mtx.sign(private_key_1)
mtx.sign(private_key_2)

# print encoded transaction
print(encoding.msgpack_encode(mtx))

# send the transaction
transaction_id = acl.send_raw_transaction(encoding.msgpack_encode(mtx))
print("\nTransaction was sent!")
print("Transaction ID: " + transaction_id + "\n")