import random

input1 = 0

while True:
    try:
        input1 = int(input('How many characters in your password?: '))
        break
    except ValueError:
        print('\nPlease enter an integer.\n')

print("\nYour password length will be:",input1)

keys = []
# declare your list 

def genPassword(keys, pw):
    # clone a list 
    keys.extend(pw)
    return keys

# ['A','B','C' ,'D', 'E', 'F', 'G' ,'H' ,'I' ,'K', 'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T','V' ,'X' ,'Y' ,'Z' ,'a','b','c' ,'d', 'e', 'f', 'g' ,'h' ,'i' ,'k', 'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t','v' ,'x' ,'y' ,'z','&','!','#','$','%','&','(',')','*','+','-','.','/',':','<','=','>',',','@','[',']','^','_','`','{','|','}','~']

genPassword(keys, ['A','B','C' ,'D', 'E', 'F', 'G' ,'H' ,'I' ,'K', 'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T','V' ,'X' ,'Y' ,'Z' ,'a','b','c' ,'d', 'e', 'f', 'g' ,'h' ,'i' ,'k', 'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t','v' ,'x' ,'y' ,'z','&','!','#','$','%','&','*','+','-','.','/',':','<','=','>',',','@','[',']','^','_','`','{','|','}','~'])

pw = [random.choice(keys) for i in range(input1)]

password_string = ''.join(pw)
print("\nYour password will be:\n",password_string)  


