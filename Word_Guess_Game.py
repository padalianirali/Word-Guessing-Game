#importing required library 
import random

#getting naame of the player and initiating the game
name = input("Hi! May I know your name please?\n")
print("Hi",name,"Let's Play!\n")

#list of colors
words = ['green','pink','blue','white','grey','black','red','purple','maroon','yellow','orange','golden','silver','brown','navy']

#using 'choice' method of the random package to arbitrarily choose the color from the defined list of colors 
word = random.choice(words)

#asking player to start guessing
print("Guess a word")

#initializing variables to keep track of total guesses made and total turns available
guesses = ''
turns = 10

#defining the game 
while turns > 0:
    
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
            
    if failed == 0:
        print("Congratulations! You won. The word is",word)
        break
    
    attempt = input("\nGuess any character:\n")
    print("\n")
    
    guesses += attempt

    if attempt not in word:
        turns -=1
        print("Oops! You have",str(turns),"attempts left!\n")
 
        if turns == 0 :
            print("Sorry! You lost the game. The word is",word)
        
        

