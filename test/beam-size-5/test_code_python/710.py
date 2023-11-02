def solution():
    
    cost_per_pound = 20
    cost_per_pound_of_blueberries = 1.5
    pounds_of_blueberries = 30
    total_cost = cost_per_pound_of_blueberries * pounds_of_blueberries
    savings = total_cost - cost_per_pound_of_blueberries
    result = savings
    return result

print(solution())