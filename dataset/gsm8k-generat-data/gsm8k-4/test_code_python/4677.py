def solution():
    """For a fundraiser, Nellie needs to sell 45 rolls of gift wrap. So far, she has sold 1 roll to her grandmother, 10 rolls to her uncle, and 6 rolls to a neighbor. How many more rolls of gift wrap does Nellie need to sell?"""
    # Define the number of rolls sold
    rolls_sold = 1 + 10 + 6

    # Calculate the number of rolls left to sell
    rolls_left = 45 - rolls_sold

    # return the result
    result = rolls_left
    return result

print(solution())