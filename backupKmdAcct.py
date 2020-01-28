import params
from algosdk import kmd, mnemonic
from algosdk.wallet import Wallet

# create a kmd client
kcl = kmd.KMDClient(params.kmd_token, params.kmd_address)

# wallet = Wallet("wallet_name", "wallet_password", kcl)

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

accounts = kcl.list_keys(wallethandle)
print("Accounts:", accounts)
accountkey = kcl.export_key(wallethandle, "testpassword", "WHWPLXPIANMRNFB6ZEBJKXMZWRN4NLDK3BNVNOIEEAEUWIJDFVNHNPA3OQ")
print("Account Key:", accountkey)
mn = mnemonic.from_private_key(accountkey)
print("Mnemonic: ", mn)

# wallethandle = wallet.init_handle()
# print("Wallet Handle:", wallethandle)