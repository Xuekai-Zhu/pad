def solution():
    """John buys 2 pairs of shoes for each of his 3 children. They cost $60 each. How much did he pay?"""
    num_children = 3
    num_shoes_per_child = 2
    cost_per_shoe = 60
    total_cost = num_children * num_shoes_per_child * cost_per_shoe
    result = total_cost
    return result

print(solution())