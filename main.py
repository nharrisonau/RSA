import random

def is_prime(n, tests=10):
    """Miller-Rabin primality test."""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(tests):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(key_size=1024):
    """Generate a random large prime number."""
    while True:
        num = random.getrandbits(key_size)
        if is_prime(num):
            return num

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a, b):
    """Extended Euclidean Algorithm for finding modular inverse."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean_algorithm(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    """Modular inverse using the extended Euclidean algorithm."""
    g, x, y = extended_euclidean_algorithm(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def generate_keypair(key_size=1024):
    """Generate RSA key pair."""
    p = generate_large_prime(key_size // 2)
    q = generate_large_prime(key_size // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = modinv(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    """Encrypt a message with a public key."""
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    """Decrypt a message with a private key."""
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    print("Generating RSA key pair...")
    public, private = generate_keypair(1024)
    print("Public key:", public)
    print("Private key:", private)

    message = 'This is a secret message.'
    print("Original:", message)

    encrypted_msg = encrypt(public, message)
    print("Encrypted:", ''.join(map(lambda x: str(x), encrypted_msg)))

    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted:", decrypted_msg)
