def solution():
    cost_last_year = 1800
    decrease_fraction = 2/5
    cost_now = cost_last_year / (1 - decrease_fraction)
    num_lawnmowers = 4
    total_cost = cost_now * num_lawnmowers
    result = total_cost
    return result

print(solution())