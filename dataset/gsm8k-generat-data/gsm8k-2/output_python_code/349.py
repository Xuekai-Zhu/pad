def solution():
    """For a school fundraiser, Chandler needs to sell 12 rolls of wrapping paper. So far, he has sold 3 rolls to his grandmother, 4 rolls to his uncle, and 3 rolls to a neighbor. How many more rolls of wrapping paper does Chandler need to sell?"""
    total_rolls = 12
    sold_rolls = 3 + 4 + 3
    remaining_rolls = total_rolls - sold_rolls
    result = remaining_rolls
    return result

print(solution())