def solution():
    """Betsy won 5 games of Monopoly. Helen won twice as many as Betsy and Susan won three times as many as Betsy. Between them, how many games have they won?"""
    # Define the number of games won by Betsy
    betsy_wins = 5

    # Calculate the number of games won by Helen and Susan
    helen_wins = betsy_wins * 2
    susan_wins = betsy_wins * 3

    # Calculate the total number of games won by all three
    total_wins = betsy_wins + helen_wins + susan_wins

    # return the result
    result = total_wins
    return result

print(solution())