#Generate Password
import random
str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_"
len_password = int(input("Decide your password length: "))
password = "" #initialize with NULL("")

for i in range(len_password):
    password+= random.choice(str) #selects a random element from 'str' and concatenates to 'password'

print(password)













