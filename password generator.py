#nu stiu ce pula mea fac

import random
import string

#choose the lenght of the password
password_length = int(input("Enter the password lenght: "))
password = ""


letters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase #variable for letters lowercase/uppercase
numbers = string.digits #variable for numbers
symbols = string.punctuation #variable for symbols

   
for index in range(password_length):
    password = password + random.choice(letters + numbers + symbols)
print("Password generated: {}".format(password))