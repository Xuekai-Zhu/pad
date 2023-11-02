def solution():
    """Winston has 14 quarters. He then spends half a dollar on candy. How many cents does he have left?"""
    quarters = 14
    candy_cost = 50  # in cents
    cents_left = (quarters * 25) - candy_cost
    result = cents_left
    return result

print(solution())