def solution():
    """John buys cans of soup for buy 1 get one free. He gets 30 cans with a normal price of $0.60. How much does he pay?"""
    normal_price = 0.60
    num_cans = 30
    num_paid_cans = num_cans / 2
    total_cost = num_paid_cans * normal_price
    result = total_cost
    return result

print(solution())