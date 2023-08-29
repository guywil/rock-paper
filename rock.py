#libraries
import random
from tkinter import * 

#colors
gray = '#757780'
white = '#fffffc'
black = '#001011'
blue = '#6ccff6'

root = Tk()
root.title('Rock, Paper, Scissors the Game')
root.geometry('350x350')
root.configure(background = white)

possible_choice = ['rock', 'paper', 'scissors']
comp = random.choice(possible_choice)

def rock_act():
    if comp == 'rock':
        result = "Draw"
    elif comp == 'paper':
        result = 'lost to a robot :('
    elif comp == 'scissors':
        result = 'You Win!'
    
def paper_act():
    if comp =='paper':
        result = 'Draw'
    elif comp == 'scissors':
        result = 'lost to a robot :('
    elif comp == 'rock':
        result = 'You Win!'

def scis_act():
    if comp == 'scissors':
        result = 'Draw'
    elif comp == 'rock':
        result = 'you lost to a robot :('
    elif comp == 'paper':
        result = 'You Win'

# main header
head = Label(root, 
text='Rock, Paper, Scissors', 
font = ('futura', 25), 
fg = gray,
background = white)
head.pack()


frame = Frame(root)
frame.pack()

r_but = Button(frame, text = 'Rock', command = 'rock_act',
fg = blue,
highlightbackground = white,)
r_but.pack()

root.mainloop()

"""""
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
"""