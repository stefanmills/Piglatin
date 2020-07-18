import string
import random

passlen=int(input("What is the length of the password you want\n"))

letters=string.ascii_letters
digits=string.digits
symbols=string.punctuation
encrypt=[]
encrypt.extend(list(letters))
encrypt.extend(list(digits))
encrypt.extend(list(symbols))
random.shuffle(encrypt)

password="".join(encrypt[0:passlen])
print(password)