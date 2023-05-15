import random
from replit import clear
from art import logo, vs
from game_data import data

def getCeleb():
  return random.choice(data)

def display(celeb1, celeb2, isWIN = True):
  print(logo)
  if isWIN:
    print(f"You're right! Current score: {score}.")
  print(f"\nCompare A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}.")
  print(vs)
  print(f"\nAgainst B: {celeb2['name']}, a {celeb2['description']}, from {celeb2['country']}.")
  return input("\nWho has more followers? Type 'A' or 'B':")

celeb1 = getCeleb()
celeb2 = getCeleb()
score = 0
inp = display(celeb1, celeb2, False)
while True:
  if inp == 'A':
    clear()
    if celeb1['follower_count'] >= celeb2['follower_count']:
      score += 1
      celeb2 = getCeleb()
      inp = display(celeb1, celeb2)
    else:
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}.")
      break
  elif inp== 'B':
    clear()
    if celeb2['follower_count'] >= celeb1['follower_count']:
      score += 1
      celeb1 = getCeleb()
      inp = display(celeb2, celeb1)
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}.")
      break
  else:
    clear()
    print(logo)
    print("Wrong Answer!")
    break
