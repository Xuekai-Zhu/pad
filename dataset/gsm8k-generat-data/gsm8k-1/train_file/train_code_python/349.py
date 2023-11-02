def solution():
    """For a school fundraiser, Chandler needs to sell 12 rolls of wrapping paper. So far, he has sold 3 rolls to his grandmother, 4 rolls to his uncle, and 3 rolls to a neighbor. How many more rolls of wrapping paper does Chandler need to sell?"""
    total_rolls_needed = 12
    rolls_sold = 3 + 4 + 3
    rolls_left_to_sell = total_rolls_needed - rolls_sold
    result = rolls_left_to_sell
    return result

print(solution())