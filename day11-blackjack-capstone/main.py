import random

decks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
user_cards = []
computer_cards = []
user_result = 0
computer_result = 0
sum_of_cards = 0


def sum_cards(cards):
    global sum_of_cards
    for index in cards:
        print(index)
        sum_of_cards += index
    return sum_of_cards


def start_game():
    user_cards.append(random.choice(decks))
    user_cards.append(random.choice(decks))
    computer_cards.append(random.choice(decks))
    computer_cards.append(random.choice(decks))


def continue_computers_deck(computer_cards):
    random_card = random.choice(decks)
    sum_of_cards = sum_cards(computer_cards)
    if sum_of_cards < 22 & (sum_of_cards + random_card) < 22:
        computer_cards.append(random_card)
        print(computer_cards)
    else:
        return

def continue_user_deck(user_cards):
    random_card = random.choice(decks)
    sum_of_cards = sum_cards(user_cards)
    if sum_of_cards < 22:
        user_cards.append(random_card)
        print(user_cards)
    else:
        print(f" U lose")


start_game()

print(f"Your cards: [{user_cards[0], user_cards[1]}]")
print(f"Computer's first card: {computer_cards[0]} and second card {computer_cards[1]}")
continue_game = 'y'
while continue_game == 'y':
    continue_game = input("Type 'y' to get another card, type 'n' to pass: ")

    if continue_game == 'y':
        if len(user_cards) < 6:
            continue_user_deck(user_cards)
        else:
            print("You can't have more than 5 cards")
    if continue_game == 'n':
        continue_computers_deck(computer_cards)
