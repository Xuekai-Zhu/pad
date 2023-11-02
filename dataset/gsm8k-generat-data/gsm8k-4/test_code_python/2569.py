def solution():
    """Chloe and Max played Mario Kart together. The ratio of Chloe’s wins to Max’s wins is 8:3. Chloe won 24 times. How many times did Max win?"""
    # Define the ratio of Chloe's wins to Max's wins
    chloe_max_ratio = 8/3

    # Calculate the number of Max's wins
    max_wins = (24 / chloe_max_ratio) * (3/8)

    # Return the result
    result = int(max_wins)
    return result

print(solution())