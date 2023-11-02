def solution():
    """In 2010 the Chicago Bulls won 70 games. The Miami Heat won 5 more games than the Chicago Bulls.  How many games did the Bulls and the Heat win together?"""
    # Define the number of games won by the Bulls
    bulls_wins = 70

    # Calculate the number of games won by the Heat
    heat_wins = bulls_wins + 5

    # Calculate the total number of games won by both teams
    total_wins = bulls_wins + heat_wins

    # Display the total number of wins
    result = total_wins
    return result

print(solution())