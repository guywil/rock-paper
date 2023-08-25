#libraries
import random
import time

#intro to game
print("Welcome to Rock, Paper, Scissors!")
print("try and guess the winning response below")

while True:
    choice = input("choose (rock, paper, or scissors):")

    possible_choice = ['rock', 'paper', 'scissors']
#computers choosing
    computer_choice = random.choice(possible_choice)
    time.sleep(1)
    
    print(f"you chose {choice} while the super computer chose {computer_choice}")
    time.sleep(0.5)
#player choice variables
    if choice == computer_choice:
        print(f"you both selected {choice}. It's a tie ")
   
    elif choice == 'rock':
        if computer_choice == 'scissors':
            print('you win again!')
        else: print('you really lost to a  random robot :(')
    elif choice == 'paper':
        if computer_choice == 'rock':
            print('you won again!')
        else: print('you really lost to a robot :(')
    elif choice == 'scissors':
        if computer_choice == 'paper':
            print('you won again!')
        else: print('you really lost to a robot :(')
#play again or not
    play_again = input('anotha one? (yes/no):')
    if play_again == 'no':
        print('rage quit much')
        time.sleep(1)
        print('okay bye, sorry you do not want to play any more')
        break