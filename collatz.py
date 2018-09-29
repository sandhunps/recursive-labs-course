def collatz(number):
        if (number%2)==0:
            ReturnValue=(number//2)
        else:
             ReturnValue=((3*number)+1)
          
        print(ReturnValue)
        if ReturnValue != 1:
             collatz(ReturnValue)

print('enter the number.')
number=input()
collatz(int(number))



