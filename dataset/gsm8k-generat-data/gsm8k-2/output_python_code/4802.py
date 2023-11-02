def solution():
    """Hannah wanted to make an apple pie that would serve 8 people. She needed 2 pounds of apples that were on sale for $2.00 per pound. The pre-made pie crust cost $2.00. The lemon cost $.50 and the butter cost $1.50. How much did each serving of pie cost?"""
    apples_cost_per_pound = 2
    apples_weight = 2
    crust_cost = 2
    lemon_cost = 0.5
    butter_cost = 1.5
    total_cost = apples_cost_per_pound * apples_weight + crust_cost + lemon_cost + butter_cost
    cost_per_serving = total_cost / 8
    result = cost_per_serving
    return result

print(solution())