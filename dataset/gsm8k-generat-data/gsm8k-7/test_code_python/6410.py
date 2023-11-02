def solution():
    num_lines = 5

    # Calculate the cost for T-Mobile
    tmobile_cost = 50 + 16*(num_lines-2)

    # Calculate the cost for M-Mobile
    mmobile_cost = 45 + 14*(num_lines-2)

    # Calculate the difference in cost
    cost_difference = tmobile_cost - mmobile_cost
    result = cost_difference
    return result

print(solution())