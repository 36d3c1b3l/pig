import random

MAX_VAL = 6
MIN_VAL = 1
MAX_SCORE = 50

def roll():
    return random.randint(MIN_VAL, MAX_VAL)

def input_players():
    while True:
        players = input("Enter the number of players from 2 to 4: ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("Enter a number from 2-4 please")
        else:
            print("Enter a number please")   
    return players


def main():
    players = input_players()
    player_scores = [0 for _ in range(players)]
    while max(player_scores) < MAX_SCORE:
        for i in range(players):
            print(f"\nPlayer{i + 1} turn started\n")
            print(f"You total score is {player_scores[i]}")
            current_score = 0
            while True:
                should_roll = input("Would you like to roll? (y/n) ")
                if should_roll.lower() != "y":
                    break
                value = roll()
                if value == 1:
                    print("You rolled 1! Turn done!")
                    break
                else:
                    current_score += value
                    print(f"You rolled {value}!")
                print(f"Your score is {current_score}")
            player_scores[i] += current_score
            print(f"Your total score is {player_scores[i]}")

    max_score = max(player_scores)
    winning_index = player_scores.index(max_score)
    print(f"Player{winning_index + 1} wins with a score of {max_score}")
        
if __name__ == "__main__":
    main()