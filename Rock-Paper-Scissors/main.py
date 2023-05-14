rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game = [rock, paper, scissors]

while(True):
  number = int(input("\nEnter 0 for Rock, 1 for Paper, or 2 for Scissors: "))
  print("\nYou chose:\n",game[number])
  rand_num = random.randint(0,2)
  print("\nComputer chose:\n",game[rand_num])
  if((number == 2 and rand_num == 0) or (rand_num > number) and not(rand_num == 2 and number == 0)):
    print("\nYou lose")
    break
  elif(rand_num == number):
    print("\nDraw")
  else:
    print("\nYou win")
