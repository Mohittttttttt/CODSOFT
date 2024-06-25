                                #TASK2- PASSWORD GENERATOR
import random
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ,abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
symbols="!@#$%^&*()_+{}[]?/|'';:<>,."
characters=alphabets+numbers+symbols
length=int(input("Enter the length password for your password:"))
Password=''.join(random.sample(characters, length))
print("The password is:", Password)




