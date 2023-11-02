def solution():
    # Calculate the cost of the small tubs
    total_cost = 48
    large_tub_cost = 6
    num_large_tubs = 3
    cost_of_large_tubs = large_tub_cost * num_large_tubs
    cost_of_small_tubs = total_cost - cost_of_large_tubs
    num_small_tubs = 6
    cost_per_small_tub = cost_of_small_tubs / num_small_tubs
    result = cost_per_small_tub
    return result

print(solution())