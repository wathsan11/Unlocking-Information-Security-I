# Brute force a message encrypted with AES-CBC, given that it was encrypted with a key that represents a phone number of someone from Tel-Aviv, padded with zeroes (in other words, 9 digits, beginning with 036, and with trailing '0' to a length of 16 bytes, like this: 036######0000000).

# You should test your brute-force cracker code using the outputs from your encrypt function of Hackxercise 6.

# Make sure you send is_english() a properly decoded string In 'latin1')



from Crypto.Cipher import AES
from Crypto import Random
import itertools
import binascii
import sys
sys.path.insert(0,'.')
from Root.prev_func import aes_decrypt, is_english
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, k):
    IV = get_random_bytes(16)
    cipher = AES.new(k, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(plaintext)
    return (IV + ciphertext)

def aes_decrypt(ciphertext, k):
    IV = ciphertext[:16]
    true_ciphertext = ciphertext[16:]
    cipher_dec = AES.new(k, AES.MODE_CBC, IV)
    decrypted = cipher_dec.decrypt(true_ciphertext)
    return decrypted.decode('latin1')
    

def brute_force_aes(ciphertext):

    
    for i in range (1000000):
        mid = str(i).zfill(6)
        key = '036'+mid+"0000000"
        
        key = key.encode("latin1")
        
        pt = aes_decrypt(ciphertext,key)
        
        if is_english(pt):
            return pt, key
    
            
    # return "", b""
    return None,None









