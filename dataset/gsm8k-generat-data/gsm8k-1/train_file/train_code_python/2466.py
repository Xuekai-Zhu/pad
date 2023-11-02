def solution():
    """Betsy won 5 games of Monopoly. Helen won twice as many as Betsy and Susan won three times as many as Betsy. Between them, how many games have they won?"""
    betsy_wins = 5
    helen_wins = 2 * betsy_wins
    susan_wins = 3 * betsy_wins
    total_wins = betsy_wins + helen_wins + susan_wins
    result = total_wins
    return result

print(solution())