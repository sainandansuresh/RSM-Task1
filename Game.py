#Rock paper scissor game
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
computer_points = 0
Nandan_points = 0
while True:
    player = input("Lets go! Rock, Paper or  Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Sorry! You lose!", computer, "covers", player)
            computer_points+=1
        else:
            print("Yey! You win!", player, "smashes", computer)
            Nandan_points+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("Sorry! You lose!", computer, "cut", player)
            computer_points+=1
        else:
            print("Yey! You win!", player, "covers", computer)
            Nandan_points+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("Sorry! You lose...", computer, "smashes", player)
            computer_points+=1
        else:
            print("Yey! You win!", player, "cut", computer)
            Nandan_points+=1
    elif player=='end':
        print("The Final Points are:")
        print(f"Computer:{computer_points}")
        print(f"Nandan:{Nandan_points}")
        break