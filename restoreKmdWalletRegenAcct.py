import params
from algosdk import kmd, mnemonic

# create a kmd client
kcl = kmd.KMDClient(params.kmd_token, params.kmd_address)

# get the master derivation key from the mnemonic
backup = "alpha worry field wait hobby artist grape engine sponsor broccoli scare thing bean kind say royal inmate hood situate lock benefit omit index about usual"
mdk = mnemonic.to_master_derivation_key(backup)

# recover the wallet by passing mdk when creating a wallet
new_wallet = kcl.create_wallet("wallet21", "testpassword", master_deriv_key=mdk)
print("New Wallet:", new_wallet)

walletid = new_wallet.get("id")
print(walletid)

wallethandle = kcl.init_wallet_handle(walletid, "testpassword")
accounts = kcl.list_keys(wallethandle)
print("Accounts:", accounts)

# if there were accounts previously generated in this wallet, then generate_key() will regenerate them
address = kcl.generate_key(wallethandle)
print("New account:", address)
