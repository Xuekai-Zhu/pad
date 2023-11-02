def solution():
    # Calculate the number of ties
    ties = 12 / 2

    # Calculate the total number of non-win games
    non_win_games = 12 + ties

    # Calculate the number of wins
    wins = 56 - non_win_games
    result = wins
    return result

print(solution())