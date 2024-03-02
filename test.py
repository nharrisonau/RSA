from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Assuming you have the 'encrypt' and 'decrypt' functions from the previous example
# And assuming 'public_key' and 'private_key' are RSA keys generated from the previous example's 'generate_keypair' function

# Generate RSA keys using PyCryptodome
key = RSA.generate(1024)
private_key_pycrypto = key.export_key()
public_key_pycrypto = key.publickey().export_key()

cipher_pycrypto = PKCS1_OAEP.new(key)

# Encrypt the message using the custom RSA implementation
custom_encrypted_msg = encrypt(public_key, 'This is a secret message.')

# Encrypt the message using PyCryptodome's RSA implementation
pycrypto_encrypted_msg = cipher_pycrypto.encrypt(b'This is a secret message.')

# Decrypt the message using the custom RSA implementation
custom_decrypted_msg = decrypt(private_key, custom_encrypted_msg)

# Decrypt the message using PyCryptodome's RSA implementation
cipher_pycrypto_decrypt = PKCS1_OAEP.new(RSA.import_key(private_key_pycrypto))
pycrypto_decrypted_msg = cipher_pycrypto_decrypt.decrypt(pycrypto_encrypted_msg)

# Compare the results
print("Custom Decrypted:", custom_decrypted_msg)
print("PyCryptodome Decrypted:", pycrypto_decrypted_msg.decode('utf-8'))

# Note: Direct comparison of encrypted messages may not be meaningful due to padding and other factors.
