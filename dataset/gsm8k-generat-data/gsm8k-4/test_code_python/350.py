def solution():
    """For a school fundraiser, Chandler needs to sell 12 rolls of wrapping paper. So far, he has sold 3 rolls to his grandmother, 4 rolls to his uncle, and 3 rolls to a neighbor. How many more rolls of wrapping paper does Chandler need to sell?"""
    # Define the total number of rolls Chandler needs to sell
    total_rolls = 12

    # Calculate the number of rolls sold so far
    sold_rolls = 3 + 4 + 3

    # Calculate the number of rolls Chandler still needs to sell
    remaining_rolls = total_rolls - sold_rolls

    # return the result
    result = remaining_rolls
    return result

print(solution())