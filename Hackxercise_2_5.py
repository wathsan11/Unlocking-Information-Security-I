# Use PyCryptoDome to build the real version of the last hackxercise: implement a function encrypt that given a plaintext and a 32-bytes key k , returns a ciphertext encrypted with the actual RC4 cipher.

# Note: Follow this guide to install/upgrade pip.
# You should be on version 19.3.1 or later.
# Then install pycryptodome.

from Crypto.Cipher import ARC4

def rc4(plaintext, key):
    key = key.encode()      #convert string → bytes 
    cipher = ARC4.new(key)   
    
    ciphertext = cipher.encrypt(plaintext)
    
    return ciphertext
 # return ciphertext
