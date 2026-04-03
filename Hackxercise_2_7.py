# Implement heuristic plaintext detection using frequency analysis:

# Implement a function is_english that:

# Receives a string
# Makes sure it consists of only ASCII characters (using the provided is_ascii() function)
# Counts the 3 most frequent letters in it
# Makes sure they're one of the 6 most frequent letters in English (e, t, a, o, i, n)


from collections import Counter

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    
    if not is_ascii(s):
        return False
    
    else :
        # for char in s:
        s = ''.join(x.lower() for x in s if x.isalpha())
        #   if not char.isalpha():
        #         s = s.replace(char,"")
            
        # s = s.lower()
        if not s:
            return False
            
            
        counts = Counter(s)
        
        top3 = counts.most_common(3)
    
    # return a
        
        for c,_ in top3:
            if c not in ('e', 't', 'a', 'o', 'i', 'n'):
                return False
        return True
    
     # return boolean
     
     
# print(is_english("earieiaaooo"))
