# Write a XOR cipher: implement a function encrypt that given a plaintext string and a key  (also a string), returns a ciphertext where each character is XORed with its respective character in . Assume that the plaintext and key have the same length. (that is, plaintext[i] is XORed with k[i]).

def encrypt(plaintext, k):
   
    if(len(plaintext)!=len(k)):
        return
    

    ciphertext = ""
        
    for p,c in zip(plaintext,k):
        cipherchar = chr(ord(p)^ord(c))
        ciphertext+=cipherchar
            
    return ciphertext # Do stuff and return ciphertext
