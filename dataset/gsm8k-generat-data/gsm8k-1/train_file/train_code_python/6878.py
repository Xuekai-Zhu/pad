def solution():
    """Louise is in a toy store. She already has 28 toys worth $10 each in her cart. On her way to the till she adds 20 teddy bears to the cart. If the $580 in Louise’s wallet is exactly enough to pay for all the toys, how much does each teddy bear cost?"""
    total_toys = 28 + 20
    total_cost = 580
    cost_per_toy = 10
    cost_of_initial_toys = 28 * cost_per_toy
    remaining_cost = total_cost - cost_of_initial_toys
    cost_per_teddy_bear = remaining_cost / 20
    result = cost_per_teddy_bear
    return result

print(solution())