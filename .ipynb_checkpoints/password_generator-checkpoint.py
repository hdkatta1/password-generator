import random
import string

length = int(input("Enter the length of your password: "))
chars = string.ascii_letters
digits = string.digits
symbols = string.punctuation.replace("'", "")

password = "".join(random.choices(chars + digits + symbols, k=length)) 
#random.choices function to randomly select characters from these three sets of characters
#k=length argument specifies how many characters to choose

print("Your generated password is: ", password)
