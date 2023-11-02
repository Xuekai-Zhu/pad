def solution():
    """Chloe and Max played Mario Kart together. The ratio of Chloe’s wins to Max’s wins is 8:3. Chloe won 24 times. How many times did Max win?"""
    # Calculate the total number of wins according to the ratio
    total_wins = 8 + 3

    # Calculate the fraction of wins that Max has
    max_fractions = 3/total_wins

    # Calculate the number of wins that Max has
    max_wins = max_fractions * 24 / (1/total_wins)

    # Display the number of wins that Max has
    result = max_wins
    return result

print(solution())