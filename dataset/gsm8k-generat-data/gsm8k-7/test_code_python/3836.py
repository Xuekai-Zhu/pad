def solution():
    total_cost = 85
    num_expensive_shirts = 3
    expensive_shirt_cost = 15

    # Calculate the total cost of the remaining shirts
    remaining_shirt_cost = total_cost - (num_expensive_shirts * expensive_shirt_cost)

    # Calculate the cost of one remaining shirt
    num_remaining_shirts = 5 - num_expensive_shirts
    cost_per_remaining_shirt = remaining_shirt_cost / num_remaining_shirts
    result = cost_per_remaining_shirt
    return result

print(solution())