import random
print('Number Guessing Game')
Cguess = int(random.randint(1,10))
print(Cguess)
nturns = int(0)

while nturns < 4 :
    nturns = nturns + 1
    myguess = int(input('Enter your guess:- '))  
    if Cguess == myguess:
        print('Your guess is right. Congratulation')
        break
    elif Cguess > myguess:
        print('Your guess is too low')
    elif Cguess < myguess:
        print('Your guess is too high')
if nturns >= 4:
    print('You loss')

















