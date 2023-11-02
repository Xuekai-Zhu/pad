def solution():
    # Calculate the number of games won by each player
    phil_wins = 12
    charlie_wins = phil_wins - 3
    dana_wins = charlie_wins + 2
    perry_wins = dana_wins + 5

    # Calculate the difference in wins between Perry and Phil
    difference = perry_wins - phil_wins
    result = difference
    return result

print(solution())