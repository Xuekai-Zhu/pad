def solution():
    total_games = 50  # Including the 10 games left
    win_percentage = 0.7

    # Calculate the number of games they have won so far
    num_wins = total_games * win_percentage

    # Calculate the number of games they need to win to reach a 60% win rate
    num_wins_needed = total_games * 0.6

    # Calculate the number of games they can afford to lose
    num_losses_allowed = num_wins - num_wins_needed

    result = num_losses_allowed
    return result

print(solution())