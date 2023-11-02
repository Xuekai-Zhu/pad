def solution():
    """John Smith buys 3 cakes for $12 each and splits the cost with his brother. How much did he pay?"""
    num_cakes = 3
    cost_per_cake = 12
    total_cost = num_cakes * cost_per_cake
    split_cost = total_cost / 2
    result = split_cost
    return result

print(solution())