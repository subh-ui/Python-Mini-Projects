# Using 'string' modules

import string
import random

new_password = "" # Initialize 'new_password' with NULL("")
size_password = ""

if __name__ == "__main__":
    set_1 = string.ascii_lowercase
    set_2 = string.ascii_uppercase
    set_3 = string.digits
    set_4 = string.punctuation

    len_password = input("ENTER LENGTH OF YOUR PASSWORD: ") #To_do_1: Gibberish 
    
    if(len_password.isdigit()):
        size_password = int(len_password)
    else:
        print("Input is not a number--> >>>RE-ENTER!<<<")

    s = [] # Empty List
    s.extend(list(set_1)) # 'extend()' is a list property 
    s.extend(list(set_2)) 
    s.extend(list(set_3)) 
    s.extend(list(set_4)) 
    
    random.shuffle(s) # Increase hardness of password
    
    print("".join(random.sample(s, size_password))) #random.sample(m,n) chooses and concatenates unique characters
