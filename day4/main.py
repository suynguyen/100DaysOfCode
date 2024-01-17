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

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors"))

random = random.randint(0, 2)
if random == 0:
    print(rock)
elif random == 1:
    print(paper)
elif random == 2:
    print(scissors)
else:
    print("error")

if user_choose == random:
    print("even, so try again")

print("Computer choose")
user_choose_as_String = str(user_choose)
computer_choose_as_String = str(random)
choose = computer_choose_as_String + user_choose_as_String
user_win = "\n You win"
user_lose = "\n You lose"
if choose == "01":
    print(paper + user_win)
elif choose == "02":
    print(scissors + user_lose)
elif choose == "10":
    print(rock + user_lose)
elif choose == "12":
    print(scissors + user_win)
elif choose == "20":
    print(rock + user_win)
elif choose == "21":
    print(paper + user_lose)

