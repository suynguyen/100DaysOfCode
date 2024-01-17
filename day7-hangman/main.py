import random
import sys

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = ["house", "school", "work"]

chosen_word = random.choice(word)

blanks = []
for _ in range(len(chosen_word)):
    blanks.append("_")
print(blanks)

guess_attempt = 0
while "_" in blanks:
    print(chosen_word)
    input_letter = input("letter: ").lower()
    if input_letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if input_letter == letter:
                blanks[position] = letter
                print(blanks)
    else:
        if guess_attempt <= len(chosen_word):
            print(stages[len(chosen_word) - guess_attempt])
            guess_attempt += 1
        else:
            print(" Unfortunately you loose this time")
            sys.exit()


print("u won")
