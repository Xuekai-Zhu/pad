def solution():
    """Bill has played 200 games of poker and won 63% of them. If he plays 100 more games and loses 43 of them, what is his new win percentage?"""
    # Define the initial number of games played and won
    initial_games = 200
    initial_wins = 0.63 * initial_games

    # Define the new number of games played and won
    new_games = initial_games + 100
    new_wins = initial_wins + (new_games - initial_games - 43)

    # Calculate the new win percentage
    new_win_percentage = new_wins / new_games

    # Display the new win percentage
    result = new_win_percentage
    return result

print(solution())