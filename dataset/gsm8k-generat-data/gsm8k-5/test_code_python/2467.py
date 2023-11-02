def solution():
    betsy_wins = 5  # Betsy won 5 games of Monopoly
    helen_wins = 2 * betsy_wins  # Helen won twice as many as Betsy
    susan_wins = 3 * betsy_wins  # Susan won three times as many as Betsy

    # Calculate the total number of games won by all three of them
    total_wins = betsy_wins + helen_wins + susan_wins
    result = total_wins
    return result

print(solution())