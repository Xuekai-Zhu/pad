def solution():
    """James can buy a new computer for $600 and have it last 6 years, or buy 2 used computers for $200 each that each last 3 years. How much money will he save by picking the cheaper option?"""
    new_cost = 600
    used_cost = 400 # 2 used computers at $200 each
    years_new = 6
    years_used = 3
    cost_per_year_new = new_cost / years_new
    cost_per_year_used = used_cost / years_used
    savings = cost_per_year_new - cost_per_year_used
    result = savings
    return result

print(solution())