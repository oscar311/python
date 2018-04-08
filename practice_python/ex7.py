#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

import random

def main():

    nums = ["rock", "paper", "scissors"]

    print("Welcome to the Rock-Paper-Scissors game")

    pick = str(raw_input("Type new game to start a new game\nPress q to quit:\n"))

    while pick != "q":
        if pick == "new game":
            p = str(raw_input("Rock-Paper-Scissors: "))

            while p != "q":
                x = random.choice(nums)
                if p == x:
                    print("Draw")
                elif p == "rock" and x == "scissors":
                    print("Rock beats scissors, Player wins!")
                    break 
                elif p == "scissors" and x == "paper":
                    print("Scissors beats paper, Player wins!")
                    break
                elif p == "paper" and x == "rock":
                    print("Paper beats rock, Player wins!")
                    break
                elif x == "rock" and p == "scissors":
                    print("Rock beats scissors, Bot wins!")
                    break 
                elif x == "scissors" and p == "paper":
                    print("Scissors beats paper, Bot wins!")
                    break
                elif x == "paper" and p == "rock":
                    print("Paper beats rock, Bot wins!")
                    break


                p = str(raw_input("Rock-Paper-Scissors: "))




main()