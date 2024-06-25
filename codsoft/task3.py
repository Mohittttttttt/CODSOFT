                    #   ROCK PAPER SCISSORS GAME 

print("       ________WELCOME TO THE GAME________          ")
print("COMMAND: \n1. Rock beats scissors. \n2. Scissors beat paper. \n3. Paper beats Rock.")
import random
user_choice=int(input(" Type 0 for Rock \n Type 1 for Paper \n Type 2 for Scissors \n Enter the your choice : "))
if user_choice>=3 or user_choice<0:
    print("Please enter a valid number(0,1,2) ant try again!!")
else:
    computer_choice=random.randint(0,2)
    print("Computer choice : ",computer_choice)
    if computer_choice==user_choice:
        print("it is a tie!!")
    elif computer_choice==0 and user_choice==2:
        print("ops! You lose")
    elif user_choice==0 and computer_choice==2:
        print("Yah!You Win!!")
    elif computer_choice<user_choice:
        print("Yah!You Win!!")
    elif computer_choice>user_choice:
        print("ops! You Lose ")


