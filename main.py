import random

def roll():
    min_value = 1
    max_value = 6
    roll =  random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players 2-4: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players .")
    else:
        print("Invalid number of players")

max_score = 50
player_Scores = [0 for _ in range(players)]

while max(player_Scores) < max_score:

    for player_idx in range(players):
        print("\nplayer", player_idx, + 1, "turn has started!")
        print("your total score is:", player_Scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("you rolled 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a:", value)

                print("your score is:", current_score)

            player_Scores[player_idx] += current_score
            print("your total score is", player_Scores[player_idx])

        max_score = max(player_Scores)
        winning_idx = player_Scores.index(max_score)
        print("player number", winning_idx + 1, "is the winner with the score of:", max_score)

