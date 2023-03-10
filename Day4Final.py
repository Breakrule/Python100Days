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

# Write your code below this line 👇
map_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("Your type invalid. You lose!.")
else:
    print(map_list[user_choice])

    com_choice = random.randint(0, (len(map_list) - 1))
    print("Computer choose:\n")
    print(map_list[com_choice])

    if user_choice == 0 and com_choice == 2:
        print("You win!.")
    elif com_choice == 0 and user_choice == 2:
        print("You lose")
    elif com_choice > user_choice:
        print("You lose")
    elif user_choice > com_choice:
        print("You win")
    elif com_choice == user_choice:
        print("Draw")
