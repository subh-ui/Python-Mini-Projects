'''
-1 for Snake
0 for Water
1 for Gun

Similar as Rock, Paper, Scissors Game.
'''
import random 
guess = "SWG"

for i in range(len(guess)):
    Computer= random.choice(guess)

Player= input("Enter Your Choice: S or W or G \n")

dict= {"S": -1,
       "W": 0,
       "G": 1
    }

n= dict[Computer]
num= dict[Player]

print(f"Your Choice is {Player} \nComputer Choice is {Computer} \n")

if(n==-1 and num==0):
    print("Computer Wins \nYou Lose!")
elif(n==0 and num==-1):
    print("You Wins \nComputer Lose!")
elif(n==0 and num==1):
    print("Computer Wins \nYou Lose!")
elif(n==1 and num==0):
    print("You Wins \nComputer Lose!")
elif(n==1 and num==-1):
    print("Computer Wins \nYou Lose!")
elif(n==-1 and num==1):
    print("You Wins \nComputer Lose!")
else:
    print("TIE!")