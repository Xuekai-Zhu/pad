def solution():
    """A basketball team played 40 games and won 70% of the games. It still had 10 games to play. How many games can they lose to win 60% of their games?"""
    # Define the initial number of games played and won
    initial_games_played = 40
    initial_games_won = int(0.7 * initial_games_played)

    # Define the total number of games and the target winning percentage
    total_games = initial_games_played + 10
    target_percentage = 0.6

    # Determine the minimum number of games the team can lose and still achieve the target winning percentage
    target_wins = int(target_percentage * total_games)
    minimum_losses = initial_games_played + 10 - target_wins - initial_games_won

    # return the result
    result = minimum_losses
    return result

print(solution())