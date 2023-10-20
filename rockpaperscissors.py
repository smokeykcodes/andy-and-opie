import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input ("Enter a choice (rock, paper, or scissors): ")
    computer_choice = random.choices (options)
    #Look here...
    computer_choice2 = str(computer_choice[0])
    choices = {"player" : player_choice, "computer" : computer_choice2}
    
    return choices

def check_win(player, computer):
    print (f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors! YOU WIN!"
        else:
            return "YOU LOSE"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! YOU WIN!"
        else:
            return "YOU LOSE"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! YOU WIN!"
        else:
            return "YOU LOSE"

choices = get_choices()
result = check_win (choices ["player"], choices ["computer"])
print (result)
