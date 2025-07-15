'''
-1 for Snake
0 for Water
1 for Gun

Similar as Rock, Paper, Scissors Game.
'''

Computer= input("Enter Your Choice: S or W or G \n")
Player= input("Enter Your Choice: S or W or G \n")

dict= {"S": -1,
       "W": 0,
       "G": 1
    }

n= dict[Computer]
num= dict[Player]

if(n==-1 and num==0):
    print("Computer Wins \n You Lose!")
elif(n==0 and num==-1):
    print("You Wins \n Computer Lose!")
elif(n==0 and num==1):
    print("Computer Wins \n You Lose!")
elif(n==1 and num==0):
    print("You Wins \n Computer Lose!")
elif(n==1 and num==-1):
    print("Computer Wins \n You Lose!")
elif(n==-1 and num==1):
    print("You Wins \n Computer Lose!")
else:
    print("TIE!")