def solution():
    """James can buy a new computer for $600 and have it last 6 years, or buy 2 used computers for $200 each that each last 3 years. How much money will he save by picking the cheaper option?"""
    new_cost = 600
    used_cost = 2 * 200
    new_lifespan = 6
    used_lifespan = 3
    new_cost_per_year = new_cost / new_lifespan
    used_cost_per_year = used_cost / (2 * used_lifespan)
    savings = new_cost_per_year - used_cost_per_year
    result = savings
    return result

print(solution())