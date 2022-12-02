# Rock Paper Scissors Game -
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

rps_list = [rock, paper, scissors]
choice = len(rps_list)
computer_choice = random.randint(0,choice-1)
computer = rps_list[computer_choice]
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
human = rps_list[human_choice]

print(f"You chose:\n{human}")
print(f"Computer chose:\n{computer}")
if computer_choice == 0 and human_choice == 2:
    print("You lose")
elif computer_choice == 1 and human_choice == 0:
    print("You lose")
elif computer_choice == 2 and human_choice == 1:
    print("You lose")
elif computer_choice == human_choice:
    print ("Draw")
else:
    print("You Win")