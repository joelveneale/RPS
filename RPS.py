import random

print("Lets Play Rock, Paper, Scissors")

rock = 0
paper = 1
scissors = 2

gamecount = input('How many games shall we play?')


while gamecount > 0:

  minmax = [0, 1, 2]

  computers_choice = random.randit(0, 2)
  users_choice = input("Roshambo!! Press 0 for Rock, 1 for Paper and 2 for Scissors!! ")

  if computers_choice == 0 & users_choice == 0:
      print("You both threw ROCK, go again... ")
  elif computers_choice == 1 & users_choice == 1:
      print("You both threw PAPER, go again... ")
  elif computers_choice == 2 & users_choice == 2:
      print("You both threw SCISSORS, go again... ")

  elif computers_choice == 0 & users_choice == 1:
      print("PAPER COVERS ROCK -- YOU WIN!")
      gamecount = gamecount - 1
  elif computers_choice == 0 & users_choice == 2:
      print("ROCK SMASHES SCISSORS -- YOU LOSE :( ")
      gamecount = gamecount - 1
  elif computers_choice == 1 & users_choice == 0:
      print("PAPER COVERS ROCK -- YOU LOSE :( ")
      gamecount = gamecount - 1
  elif computers_choice == 1 & users_choice == 2:
      print("SCISSORS CUT PAPER -- YOU WIN!")
      gamecount = gamecount - 1
  elif computers_choice == 2 & users_choice == 0:
      print("ROCK SMASHES SCISSORS -- YOU WIN!")
      gamecount = gamecount - 1
  elif computers_choice == 2 & users_choice == 1:
      print("SCISSORS CUT PAPER -- YOU LOSE :( ")
      gamecount = gamecount - 1
  else:
      users_choice not in minmax:
      print("Press 0 for Rock, 1 for Paper and 2 for Scissors ")





