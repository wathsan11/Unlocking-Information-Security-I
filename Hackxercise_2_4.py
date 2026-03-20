# Write the stream cipher fake-RC4: implement a function encrypt that given a plaintext and a 32-bytes key k, returns a ciphertext encrypted with a weak variant of RC4 which we describe here.

# First, implement the fake-RC4 pseudo-random generator (PRG):

# It starts with i=j=0 , and to generate the next byte in the keystream it:
# Increments i by  1(modulo 32),
# Increments j by the i^th character of the key (modulo 32),
# Swaps the i^th character of the key with its j^th character,
# Adds the i^th character of the key and its j^th character, modulo 32, and returns the key's character at that index.
# So for example, if the i^th character of the key was 'a' (whose ASCII value is 97), and its j^th character was '3' (whose ASCII value is 51), their sum would be 148. Modulo the length of the key, the result will be 148%32=20, so the pseudo random generator would return the 2o^th character of the key as the next byte.

# Once you have the pseudo-random generator working, the rest is easy:

# Iterate over the plaintext
# XOR every character with the next byte of the pseudo-random generator's keystream
# Return the result as the ciphertext!

def get_prg(plaintext_size, k):
    list_k = list(k)
    keystream = ""
    i=0
    j = 0
    n = len(list_k)
    while(len(keystream)<plaintext_size):
        
        # Convert characters to ASCII ---> ord()
        i=(i+1)%n
        j=(j+ord(list_k[i]))%n
        list_k[i],list_k[j]= list_k[j],list_k[i]
        x = (ord(list_k[i])+ord(list_k[j]))%n
        keystream += list_k[x]
        
    return keystream    
     # return keystream

def fake_rc4(plaintext, keystream):
    
    ciphertext = ""
    for k,p in enumerate(plaintext):
        c = keystream[k]
        cipherChr = chr(ord(p)^ord(c))
        ciphertext+=cipherChr
        
    return ciphertext # return ciphertext
