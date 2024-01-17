#!/usr/bin/env python3
from ecdsa import SigningKey, SECP256k1
import hashlib

# Generate private key using ECDSA.
private_key = SigningKey.generate(curve=SECP256k1)

# Convert the private key to hexadecimal format.
private_key_hex = private_key.to_string().hex()

# Generate public key.
public_key = private_key.get_verifying_key()

# Convert the public key to byte format.
public_key_bytes = public_key.to_string("uncompressed")

# Convert the public key to hexadecimal format.
public_key_hex = public_key_bytes.hex()

# Create ICON hx address. Apply SHA3-256 hash excluding the first byte of the public key.

hx_address = f"hx{hashlib.sha3_256(public_key_bytes[1:]).digest()[-20:].hex()}"

print("This example is an example of creating a private key and public key using 'ecdsa'.")
print(f"Private Key (Hex): {private_key_hex}")
print(f"Public Key (Hex): {public_key_hex}")
print(f"ICON Hx Address: {hx_address}")
