import random

# This function generates the AI's choice, asks the player for their choice,
# makes sure that the player's choice is a valid option, announces the AI's choice, then calls the decide function 
def rungame():
  generatednum = random.randint(1,3) # randomly generates a number between 1 and 3
  if generatednum == 1: # if-else chain to change numbers to options 
    generatednum = "rock"
  elif generatednum == 2:
    generatednum = "paper"
  elif generatednum == 3:
    generatednum = "scissors"
  choice = str(input("Rock, Paper, or Scissors?  # asks player for their choice
  choiceslist = ["rock", "paper", "scissors"]
  while choice.lower() not in choiceslist: # makes sure the player's choice is a valid option
    print("That's not an option!")
    choice = str(input("Rock, Paper, or Scissors? "))
  print("Your opponent chose "+ generatednum +".") # lets the player know what their opponent chose
  decide(generatednum, choice) # calls the decide function to determine the winner

# This function compares the player's choice with the AI's choice and decides the winner
def decide(generatednum, choice):
  choice = choice.lower()
  if generatednum == "rock": # nested if-else chain to conclude the winner
    if choice == "rock":
      print("Tie!")
    elif choice == "paper":
      print("You win! :)")
    elif choice == "scissors":
      print("You lose :(")
  elif generatednum == "paper":
    if choice == "rock":
      print("You lose :(")
    elif choice == "paper":
      print("Tie!")
    elif choice == "scissors":
      print("You win!")
  elif generatednum == "scissors":
    if choice == "rock":
      print("You win! :)")
    elif choice == "paper":
      print("You lose :(")
    elif choice == "scissors":
      print("Tie!")

runGame = True
while runGame: # while loop to decide whether to re-run the game
  rungame()
  repeat = str(input("Would you like to play again? Yes or No! "))
  if repeat.lower() == "yes":
    runGame = True
  elif repeat.lower() == "no":
    print("Thanks for playing!")
    runGame = False
