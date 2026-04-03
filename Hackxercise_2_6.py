# Use PyCrypto to encrypt and decrypt with AES-CBC:

# Implement a function encrypt, that given a plaintext and a -byte ( bit) key , picks a random -byte ( bit) IV, and returns a ciphertext encrypted with AES-CBC with the IV prepended to the ciphertext (in bytes).

# You may assume that the plaintext length (in bytes) is a multiple of 16.

# Implement a function decrypt, that given a ciphertext (as formatted by the encrypt function) and a -byte ( bit) key , returns the plaintext as decrypted by AES-CBC (in 'latin1').

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import get_random_bytes


def aes_encrypt(plaintext, k):
    IV = get_random_bytes(16)
    # S = plaintext^IV
    cipher = AES.new(k,AES.MODE_CBC,IV)
    ciphertext = cipher.encrypt(plaintext)
    return (IV+ciphertext)
    
    # return iv + ciphertext (in bytes)

def aes_decrypt(ciphertext, k):
    
    IV = ciphertext[:16]
    true_ciphertext = ciphertext[16:]
    cipher_dec = AES.new(k,AES.MODE_CBC,IV)
    decrypted = cipher_dec.decrypt(true_ciphertext)
    
    return decrypted.decode('latin1') # return plaintext (in 'latin1')
