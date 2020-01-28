import params
from algosdk import kmd, account, encoding, mnemonic

# create a kmd client
kcl = kmd.KMDClient(params.kmd_token, params.kmd_address)

walletid = None
wallets = kcl.list_wallets()
print("Wallet List:", wallets)
for arrayitem in wallets:
    if arrayitem.get("name") == "wallet1":
        walletid = arrayitem.get("id")
        break
print("Wallet ID:", walletid)

wallethandle = kcl.init_wallet_handle(walletid, "testpassword")
print("Wallet Handle:", wallethandle)

private_key, address = account.generate_account()
print("Private key:", private_key)
print("Address:", address)

mn = mnemonic.from_private_key(private_key)
print("Mnemonic", mn)

importedaccount = kcl.import_key(wallethandle, private_key)
print("Imported Account: ", importedaccount)