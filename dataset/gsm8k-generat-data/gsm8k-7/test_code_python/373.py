def solution():
    num_large_tubs = 3
    large_tub_cost = 6.0
    total_tub_cost = 48.0
    num_small_tubs = 6

    # Calculate the total cost of all large tubs
    total_large_tub_cost = num_large_tubs * large_tub_cost

    # Calculate the cost of all small tubs
    total_small_tub_cost = total_tub_cost - total_large_tub_cost

    # Calculate the cost of one small tub
    small_tub_cost = total_small_tub_cost / num_small_tubs
    result = small_tub_cost
    return result

print(solution())