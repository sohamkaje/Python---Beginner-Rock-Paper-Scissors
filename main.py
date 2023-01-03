import random

global choice
global generatednum

def rungame():
  global choice
  global generatednum
  generatednum = random.randint(1,3)
  if generatednum == 1:
    generatednum = "rock"
  elif generatednum == 2:
    generatednum = "paper"
  elif generatednum == 3:
    generatednum = "scissors"
  choice = str(input("Rock, Paper, or Scissors? "))
  choiceslist = ["rock", "paper", "scissors"]
  while choice.lower() not in choiceslist:
    print("That's not an option!")
    choice = str(input("Rock, Paper, or Scissors? "))
  print("Your opponent chose "+ generatednum +".")
  decide(generatednum, choice)
  
def decide(generatednum, choice):
  choice = choice.lower()
  if generatednum == "rock":
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
while runGame:
  rungame()
  repeat = str(input("Would you like to play again? Yes or No! "))
  if repeat.lower() == "yes":
    runGame = True
  elif repeat.lower() == "no":
    print("Thanks for playing!")
    runGame = False