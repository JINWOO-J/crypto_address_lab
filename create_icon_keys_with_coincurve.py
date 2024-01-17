#!/usr/bin/env python3
from coincurve import PrivateKey
import hashlib

# Generate private key
private_key = PrivateKey()

# Convert the private key to hexadecimal format.
private_key_hex = private_key.to_hex()

# Generate public key
public_key = private_key.public_key

# Convert public key to hexadecimal format
public_key_bytes = public_key.format(compressed=False)

public_key_hex = public_key_bytes.hex()

hx_address = f"hx{hashlib.sha3_256(public_key_bytes[1:]).digest()[-20:].hex()}"

print("This example is an example of creating a private key and public key using 'coincurve'.")
print(f"Private Key (Hex): {private_key_hex}")
print(f"Public Key (Hex): {public_key_hex}")
print(f"ICON Hx Address: {hx_address}")
