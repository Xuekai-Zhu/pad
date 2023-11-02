def solution():
    """For a school fundraiser, Chandler needs to sell 12 rolls of wrapping paper. So far, he has sold 3 rolls to his grandmother, 4 rolls to his uncle, and 3 rolls to a neighbor. How many more rolls of wrapping paper does Chandler need to sell?"""
    # Define the target number of rolls and the number sold so far
    TARGET_ROLLS = 12
    SOLD_ROLLS = 3 + 4 + 3

    # Calculate the number of rolls Chandler still needs to sell
    remaining_rolls = TARGET_ROLLS - SOLD_ROLLS

    # Display the number of rolls remaining to sell
    result = remaining_rolls
    return result

print(solution())