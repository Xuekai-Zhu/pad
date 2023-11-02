def solution():
    betsy_wins = 5
    helen_wins = betsy_wins * 2
    susan_wins = betsy_wins * 3

    # Calculate the total number of games won by all three players
    total_wins = betsy_wins + helen_wins + susan_wins
    result = total_wins
    return result

print(solution())