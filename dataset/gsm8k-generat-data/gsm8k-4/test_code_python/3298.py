def solution():
    """Bill has played 200 games of poker and won 63% of them. If he plays 100 more games and loses 43 of them, what is his new win percentage?"""
    # Define the initial number of games played and won
    initial_games = 200
    initial_wins = 0.63 * initial_games

    # Define the new number of games played and won
    new_games = 100 + initial_games
    new_wins = initial_wins - 43

    # Calculate the new win percentage
    new_win_percentage = (new_wins / new_games) * 100

    # return the result
    result = new_win_percentage
    return result

print(solution())