def solution():
    
    desired_height = 2
    growth_per_month = 0.5
    growth_per_year = growth_per_month * 12
    time_until_cut = (4 - desired_height) / growth_per_month
    cuts_per_year = 12 / time_until_cut
    cost_per_cut = 100
    total_cost_per_year = cost_per_cut * cuts_per_year
    result = total_cost_per_year
    return result

print(solution())