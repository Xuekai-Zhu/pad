def solution():
    """A set of 7 spoons costs $21. If each spoon would be sold separately, how much would 5 spoons cost?"""
    spoons_per_set = 7
    cost_per_set = 21
    cost_per_spoon = cost_per_set / spoons_per_set
    spoons_wanted = 5
    total_cost = cost_per_spoon * spoons_wanted
    result = total_cost
    return result

print(solution())