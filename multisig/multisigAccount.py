# NOT WORKING, SCRAP CODE

# import params
from algosdk import account, transaction, algod, encoding

acl = algod.AlgodClient(params.algod_token, params.algod_address)

# generate accounts and print
private_key1, account1 = account.generate_account()
private_key2, account2 = account.generate_account()
private_key3, account3 = account.generate_account()
print("Address:", account1)
print("Address:", account2)
print("Address:", account3)

# create a multisig account
version = 1  # multisig version
threshold = 2  # how many signatures are necessary
msig = transaction.Multisig(version, threshold, [account1, account2])
# print(msig.address)
print(msig.address())
input("Please go to: https://bank.testnet.algorand.network/ to fund your multisig account." + '\n' + "Press Enter to continue...")

# get suggested parameters
params = acl.suggested_params()
gen = params["genesisID"]
gh = params["genesishashb64"]
last_round = params["lastRound"]
fee = params["fee"]

txn = {
    "sender": msig.address(),
    "fee": fee,
    "last_round": last_round,
    "last_round+100": last_round+100,
    "gh": gh,
    "receiver": account3,
    "amount": 10000,
}

msigtxn = transaction.MultisigTransaction(txn, msig)
print("Msigtxn:", msigtxn)
# trying to sign a PST
# msigtxn = transaction.SignedTransaction(txn, msig.address)
# print("Msigtxn:", msigtxn)
twosigs = msigtxn.sign(private_key1)
print("Msigtxn:", twosigs)