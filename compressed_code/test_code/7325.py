def solution():
    
    price_per_pair = 10
    num_pairs = 3
    total_cost_individual = price_per_pair * num_pairs
    total_cost_discounted = total_cost_individual * 0.9
    savings = total_cost_individual - total_cost_discounted
    result = savings
    return result

print(solution())