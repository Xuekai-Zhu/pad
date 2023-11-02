def solution():
    num_roses_last_year = 12
    num_roses_this_year = num_roses_last_year / 2
    num_roses_desired = 2 * num_roses_last_year

    cost_per_rose = 3

    # Calculate the total cost of buying the remaining roses needed
    num_roses_needed = num_roses_desired - num_roses_this_year
    total_cost = num_roses_needed * cost_per_rose
    result = total_cost
    return result

print(solution())