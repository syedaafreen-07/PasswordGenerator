import random
import string as s

def passwordGenerator(length):
    char=s.ascii_letters+s.digits+s.punctuation
    password=""
    for i in range(0,length):
        password+=random.choice(char)
    return password

length=int(input("Enter the Length of the PassWord: "))
print(passwordGenerator(length))

