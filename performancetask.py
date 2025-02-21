# Rock Paper Scissor game
import random
#needed later for list usage


possibleChoices = ["rock", "paper", "scissor"]    # the options for the game 



def rps(answer): 

    userScore = 0
    dealerScore = 0 # variables that we can use later to determine who won with the highscores 
    

    rounds  = input("how much rounds do you want to play? (At most 10 rounds): ") # asks the user, how much rounds they want to play
    if int(rounds) >= 11:
        print(" Too much rounds ")# if they select a interger more than 10, the function asks again
        return rps(answer)
           
    for x in range(int(rounds) + 1): # whatever number they decided on, thats how much rounds we are playing 
        dealerChoice = random.choice(possibleChoices)# the dealer's choice is selected randomly 

        userChoice = input(f"You want {possibleChoices}?: ")# asks the user which choice they want 
                
        if userChoice == dealerChoice:
            print(f" Tie, the I chose {userChoice} aswell" ) # if the dealer and player select the same choice, its a tie 

        elif (userChoice == "rock" and dealerChoice == "scissor") or (userChoice == "paper" and dealerChoice == "rock") or (userChoice == "scissor" and dealerChoice == "paper"):
            print(f'You won, I had {dealerChoice}')
            userScore = userScore + 1
            print("USER SCORE: ", userScore)
            # here checks if the user won, then one score is added to the total score collected

        elif (dealerChoice == "rock" and userChoice == "scissor") or (dealerChoice == "paper" and userChoice == "rock") or (dealerChoice == "scissor" and userChoice == "paper"):
            print(f' HAHA, I CHOSE {dealerChoice}')
            dealerScore =dealerScore + 1 
            print("DEALER SCORE: ", dealerScore)
            # here checks if the dealer won, then one score is added to the total score collected 
    
    print("-----------------------------------------------")
    if userScore >= dealerScore: # at the end the function compare to the total scores collected to see who won
        print("you won")
        print(f'DEALER SCORE:{dealerScore}') 
        print(f'USER SCORE:{userScore}')
        # if the player has a higher score, they won
    elif userScore <= dealerScore:
        print("I WON")
        print(f'DEALER SCORE:{dealerScore}') 
        print(f'USER SCORE:{userScore}')
        # if the dealer has higher score, they won 
    elif userScore == dealerScore:
        print("tie")
        print(f'DEALER SCORE:{dealerScore}') 
        print(f'USER SCORE:{userScore}')
        #if the score is the same, its a tie
    else:
        
        
        pass



# here asks if they want to play the game, rock, paper, scissors
    # if yes, it calls the function: rps
response  =  input(" Do you want to play Rock, Paper, Scissors? Yes or no : ")
if response == "yes" :
    rps(response)
else:
    print("Try again")
    # any other answer would end the program