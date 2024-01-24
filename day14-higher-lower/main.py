import random
import game_data

game_data_len = len(game_data.data)
score = 0
continue_game = True
compare_a = game_data.data[random.randint(0, game_data_len - 1)]
compare_b = game_data.data[random.randint(0, game_data_len - 1)]

while 1:
    print(f"Compare A: {compare_a["name"]}, {compare_a["description"]}, {compare_a["country"]}")
    print(f"Against: {compare_b["name"]}, {compare_b["description"]}, {compare_b["country"]} \n")
    answer = input("Who has more followers? Type 'A' or 'B': \n")

    if (compare_a["follower_count"] > compare_b["follower_count"]) & (answer == "A"):
        score += 1
        compare_b = game_data.data[random.randint(0, game_data_len - 1)]
    elif (compare_a["follower_count"] < compare_b["follower_count"]) & (answer == "B"):
        score += 1
        compare_a = game_data.data[random.randint(0, game_data_len - 1)]
    else:
        print(f"Your score is {score}")
        break
