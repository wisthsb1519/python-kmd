from algosdk import account, encoding, mnemonic

# generate an account
private_key, address = account.generate_account()
mn = mnemonic.from_private_key(private_key)
print("Private key:", private_key)
print("Mnemonic", mn)
print("Address:", address)

# check if the address is valid
if encoding.is_valid_address(address):
    print("The address is valid!")
else:
    print("The address is invalid.")