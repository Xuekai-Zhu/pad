def solution():
    """In 2010 the Chicago Bulls won 70 games. The Miami Heat won 5 more games than the Chicago Bulls. How many games did the Bulls and the Heat win together?"""
    # Define the number of games won by the Bulls and the difference in the number of games won by the Heat
    bulls_wins = 70
    heat_wins_diff = 5

    # Calculate the number of games won by the Heat
    heat_wins = bulls_wins + heat_wins_diff

    # Calculate the total number of games won by the Bulls and the Heat
    total_wins = bulls_wins + heat_wins

    # Return the result
    result = total_wins
    return result

print(solution())