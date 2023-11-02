def solution():
    num_home_games = 56
    num_losses = 12
    num_ties = num_losses / 2

    # Calculate the number of wins by subtracting the losses and ties from the total games
    num_wins = num_home_games - num_losses - num_ties
    result = num_wins
    return result

print(solution())