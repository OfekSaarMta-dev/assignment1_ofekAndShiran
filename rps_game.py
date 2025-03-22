import json
import os


"""
    Input:
        choice1 The choice of player1 (rock, paper, or scissors).
        choice2 The choice of player2 (rock, paper, or scissors).
        player1 The name of the first player.
        player2 The name of the second player.

    Document:
        This function determines the winner of a Rock-Paper-Scissors match.
        It compares the choices of both players and returns the winner.
        If both players choose the same option, the match is a tie.

    Return:
        The name of the winning player, or "tie" if the match is a draw.
    """
def calculate_winner_in_match(choice1, choice2, player1, player2):
    rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if choice1 == choice2:
        return "tie"

    if rules[choice1] == choice2:
        return player1
    else:
        return player2


"""
    Input:
        A dictionary with player names as keys and lists as values.
        Each list contains [matches, wins, proportion] for the player.

    Document:
        Sorts the players by their win proportion and checks for a tie. 
        Returns the player with the highest proportion, or "tie" if there's a draw.

    Return:
        The name of the winner or "tie".
"""
def calculate_winner_in_game(results):
    # returning a sorted (by proportion) list of tuples [key,[matches,wins,proportions]]
    sorted_results = sorted(results.items(), key=lambda player: player[1][2], reverse=True) #[1][2] = proportion

    # To check if there is more then 1 winner. format [index in list][index in tuple(list)][index in the list(proportion)]
    if sorted_results[0][1][2] == sorted_results[1][1][2]:
        return "tie"
    else:
        return sorted_results[0][0] # returning the name of the winner

"""
    Input:
        The name of the file containing match results.

    Document:
        Reads the results from a file, processes match data, and calculates the winner based on the win ratio.
        The function returns the name of the player with the highest win ratio, or "tie" if there's no winner.
        
    Return:
        The name of the champion or "tie".
 """
def game(results_filename):
    if not os.path.exists(results_filename):
        print(f"Error: The file '{results_filename}' does not exist.")
        return None  # Exit gracefully

    results = dict()

    with open(results_filename, "r", encoding="utf8") as file:
        next(file)  # Skip header

        for line in file:
            #returning the line as words in a list
            list_of_details = line.split()
            #creating the names and choice by file format
            player1 = list_of_details[0]
            player1_choice = list_of_details[1]
            player2 = list_of_details[2]
            player2_choice = list_of_details[3]

            # Initialize players if not already in the dictionary
            results.setdefault(player1, [0, 0, 0])  # [matches, wins, win ratio]
            results.setdefault(player2, [0, 0, 0])

            # Determine the match winner
            winner = calculate_winner_in_match(player1_choice, player2_choice, player1, player2)

            if winner != "tie":
                results[winner][1] += 1  # Increase win count

            # Update match count for both players
            results[player1][0] += 1
            results[player2][0] += 1

            # Update win ratio, we will never divide by 0!!!
            results[player1][2] = results[player1][1] / results[player1][0]
            results[player2][2] = results[player2][1] / results[player2][0]

        the_champion = calculate_winner_in_game(results)

    print(f"Starting the game with {results_filename}")
    return the_champion


# Student IDs
students = {"id1": "322756586", "id2": "211449145"}

if __name__ == "__main__":
    with open("config-rps.json", "r") as json_file:
        config = json.load(json_file)

    winner = game(config["results_filename"])
    print(f"The winner is: {winner}")
