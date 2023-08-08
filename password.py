import random
import itertools
print("Welcome to the password generator")
letters=int(input("How many letters do you want in your password? "))
numbers=int(input("How many numbers do you want in your password? "))
symbol=int(input("How many symbols do you want in your password? "))
tot=letters+numbers+symbol
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num='1234567890'
s = ")!@#$%^&*(_+=-"
a=[]
b=[]
c=[]
password=[]
for i in range(letters):
    a.append(random.choice(chars))
for i in range(numbers):
    b.append(random.choice(num))
for i in range(symbol):
    c.append(random.choice(s))

i=0
j=0
l=0
k=0
while i!=tot:
    if j<letters:
        password.append(a[j])
        j+=1
        i+=1
    if l<numbers:
        password.append(b[l])
        l+=1
        i+=1
    if k<symbol:
        password.append(c[k])
        k+=1
        i+=1


print("This is the your password as per your requirements: ")
for i in range(tot):
    print(password[i],end="")

