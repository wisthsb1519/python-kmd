# this file generates standalone accounts using algosdk, creates a multisig object with those standalone accounts and imports them into a KMD wallet

import params
from algosdk import kmd, algod, account, encoding, mnemonic, transaction

# create a kmd client
kcl = kmd.KMDClient(params.kmd_token, params.kmd_address)
acl = algod.AlgodClient(params.algod_token, params.algod_address)


walletid = None
wallets = kcl.list_wallets()
# print("Wallet List:", wallets)
for arrayitem in wallets:
    if arrayitem.get("name") == "wallet1":
        walletid = arrayitem.get("id")
        break
print("Wallet ID:", walletid)
# getting wallethandle
wallethandle = kcl.init_wallet_handle(walletid, "testpassword")
print("Wallet Handle:", wallethandle)

# generate and print account 1
private_key1, address_1 = account.generate_account()
print("Private key:", private_key1)
print("Address:", address_1)

# generate and print account 2
private_key2, address_2 = account.generate_account()
print("Private key:", private_key2)
print("Address:", address_2)

# create a msig object
version = 1  # multisig version
threshold = 1  # how many signatures are necessary
msig = transaction.Multisig(version, threshold, [address_1, address_2])

# import msig object(multisig account) into kmd wallet
imported_multisig = kcl.import_multisig(wallethandle, msig)
print("Multsig Account:", imported_multisig)

# print account that are in this kmd wallet
accounts = kcl.list_keys(wallethandle)
print("Accounts:", accounts)

# print multisig accounts that are in this wallet
accounts = kcl.list_multisig(wallethandle)
print("Accounts:", accounts)