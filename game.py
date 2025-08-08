import random

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
player_answer = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")
if player_answer == 0:
    print(rock)
elif player_answer == 1:
    print(paper)
else:
    print(scissors)

game_elements = [rock, paper, scissors]
random_element = random.randint(0,2)
print("Computer chose:\n" + game_elements[random_element])
