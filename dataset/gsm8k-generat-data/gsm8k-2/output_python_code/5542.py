def solution():
    """John buys cans of soup for buy 1 get one free. He gets 30 cans with a normal price of $0.60. How much does he pay?"""
    normal_price_per_can = 0.60
    total_cans = 30
    num_paid_cans = total_cans // 2
    total_price = num_paid_cans * normal_price_per_can
    result = total_price
    return result

print(solution())