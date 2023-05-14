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

def display(number, rand_num):
  print("\nYou chose:\n",game[number])
  print("\nComputer chose:\n",game[rand_num])

while(True):
  number = int(input("\nEnter 0 for Rock, 1 for Paper, or 2 for Scissors: "))
  rand_num = random.randint(0,2)
  if(number>2 or number<0):
    print("Wrong Number, You lose!")
    break
  elif((number == 2 and rand_num == 0) or (rand_num > number) and not(rand_num == 2 and number == 0)):
    display(number, rand_num)
    print("\nYou lose")
    break
  elif(rand_num == number):
    display(number, rand_num)
    print("\nDraw")
  else:
    display(number, rand_num)
    print("\nYou win")
