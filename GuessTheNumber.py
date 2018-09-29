#This s guess the number game
import random
secretNumber =random.randint(1,20)
print('i am thinking of a number between 1 and 20')

#Ask theplayer to guess the number 6 times
for guessTaken in range(1,7):
    print('take a guess')
    guess=int(input())

    if guess <secretNumber:
        print('tour guess is to low')
    elif guess>secretNumber:
        print('your guess is too high')
    else:
        break

if guess ==secretNumber:
    print('goodjob ,youhave guessed in  '+  str(guessTaken)+ ' guessess!')
else:
    print('nope.the number i was thinking was  '+str(secretNumber))
