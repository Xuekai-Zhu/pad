def solution():
    # Calculate the number of rolls sold so far
    rolls_sold = 1 + 10 + 6  # Nellie has sold 1 roll to her grandmother, 10 rolls to her uncle, and 6 rolls to a neighbor

    # Calculate the number of rolls needed to reach the fundraising goal
    rolls_needed = 45 - rolls_sold

    result = rolls_needed
    return result

print(solution())