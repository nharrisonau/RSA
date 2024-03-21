
# Extended Euclidean Algorithm for finding modular inverse
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean_algorithm(b % a, a)
        return (g, x - (b // a) * y, y)

# Modular inverse using the extended Euclidean algorithm
def modinv(a, m):
    g, x, y = extended_euclidean_algorithm(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# Encrypt a message with a public key
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

# Decrypt a message with a private key
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    print("Generating RSA key pair...")
    p = 0x1b764263030976734cbd55898b34b833a2a4a19de5cc563d72b13e99a39270d7bd276a541fd66fe397d721368690a3b09e44905e7076cbe5edf4ba529a37b189
    q = 0xa0e5645b0abeb64f187f74d5f34748eefc15be845145c3757462207263b79a65643b13f5d049e58c75887eb28a96c537d4941a8ea3d5ae3ee4fc6f7f81835169

    e = 65537

    phi = (p-1) * (q - 1)

    n = p * q

    d = modinv(e, phi)

    public = (e, n)
    private = (d, n)

    message = 'This is a secret message.'
    print("Original:", message)

    encrypted_msg = encrypt(public, message)
    print("Encrypted:", ''.join(map(lambda x: str(x), encrypted_msg)))

    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted:", decrypted_msg)
