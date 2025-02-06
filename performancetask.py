# Rock Paper Scissor game
import random


possibleChoices = ["rock", "paper", "scissor"]


def rps(answer):

    userScore = 0
    dealerScore = 0 
    dealerChoice = random.choice(possibleChoices)
    

    rounds  = input("how much rounds do you want to play? (At most 10 rounds): ")
    if int(rounds) >= 11:
        print(" Too much rounds ")
        return rps(answer)
           
    for x in range(int(rounds) + 1):

        userChoice = input(f"You want {possibleChoices}?: ")
                
        if userChoice == dealerChoice:
            print(f" Tie, the I chose {userChoice} aswell" ) 

        elif (userChoice == "rock" and dealerChoice == "scissor") or (userChoice == "paper" and dealerChoice == "rock") or (userChoice == "scissor" and dealerChoice == "paper"):
            print(f'You won, I had {dealerChoice}')
            userScore = userScore + 1
            print("USER SCORE: ", userScore)
        elif (dealerChoice == "rock" and userChoice == "scissor") or (dealerChoice == "paper" and userChoice == "rock") or (dealerChoice == "scissor" and userChoice == "paper"):
            print(f' HAHA, I CHOSE {dealerChoice}')
            dealerScore =dealerScore + 1 
            print("DEALER SCORE: ", dealerScore)
    
    print("-----------------------------------------------")
    if userScore >= dealerScore:
        print("you won")
        print(f'DEALER SCORE:{dealerScore}') 
        print(f'USER SCORE:{userScore}')
    if userScore <= dealerScore:
        print("I WON")
        print(f'DEALER SCORE:{dealerScore}') 
        print(f'USER SCORE:{userScore}')
    if userScore == dealerScore:
        print("tie")
        print(f'DEALER SCORE:{dealerScore}') 
        print(f'USER SCORE:{userScore}')

        
        pass




response  =  input(" Do you want to play Rock, Paper, Scissors? Yes or no : ")
if response == "yes" :
    rps(response)
else:
    print("Try again")