import random


# 1 for scissors
# -1 for paper
# 0 for rock
choices= [1,-1,0]


computer = random.choice(choices)
youstr = input("Enter your choice: s/p/r ")
yourDict = {"s":1 , "p":-1, "r":0}
reverseDict = {1:"Scissors",-1:"Paper",0:"Rock"}
you = yourDict[youstr]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if(computer == you):
    print("Its a draw")
else:
    if(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")    
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Something Went wrong!")