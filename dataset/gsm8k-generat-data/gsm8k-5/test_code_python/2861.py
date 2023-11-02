def solution():
    total_games = 20 + 10  # The total number of games in the season
    required_wins = (2/3) * total_games  # The required number of wins to make the playoffs
    current_wins = 12  # The number of wins they have so far
    games_left = 10  # The number of games left in the season

    # Calculate the number of games they need to win to make the playoffs
    remaining_wins = required_wins - current_wins

    # Calculate the number of games they need to win out of the remaining games
    games_to_win = remaining_wins / games_left
    result = games_to_win
    return result

print(solution())