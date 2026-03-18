# Implement Caesar’s cipher: implement a function encrypt that given a plaintext string and a key  (how many letters to shift), returns a ciphertext where each character is shifted  places backward (so with  '' is encrypted by '')

# (You can assume all characters are lowercase letters, with no punctuation or spaces.)



alphabet = 'abcdefghijklmnopqrstuvwxyz'



def encrypt(plaintext, k):
    
    cipher_txt =""
    
    for c in plaintext:
        
        current_idx = alphabet.index(c)
        
        new_index = (current_idx - k)%26
        
        cipher_txt += alphabet[new_index]
        
    return cipher_txt
        
    # do stuff and return ciphertext
