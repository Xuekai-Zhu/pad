def solution():
    """For a fundraiser, Nellie needs to sell 45 rolls of gift wrap. So far, she has sold 1 roll to her grandmother, 10 rolls to her uncle, and 6 rolls to a neighbor. How many more rolls of gift wrap does Nellie need to sell?"""
    # Define the number of rolls sold so far
    rolls_sold = 1 + 10 + 6

    # Define the target number of rolls to sell
    target_rolls = 45

    # Calculate the number of rolls Nellie still needs to sell
    rolls_remaining = target_rolls - rolls_sold

    # Display the number of rolls remaining to sell
    result = rolls_remaining
    return result

print(solution())