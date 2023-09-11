import random

print("Welcome to the password generator")
letter=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o',
         'P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']

number=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','+','/','<','>']

letter_num=int(input('How many letters do you want?\n'))
number_num=int(input("How many numbers do you want?\n"))
symbol_num=int(input("How many symbols do you want?\n"))

password=[]
for i in range(1,letter_num+1):
    password+=random.choice(letter)

for i in range(1,number_num+1):
    password+=random.choice(number)

for i in range(1,symbol_num+1):
    password+=random.choice(symbols)
    
    random.shuffle(password)
print(''.join(password))



