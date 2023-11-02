def solution():
    """One-half of a pound of mangoes costs $0.60. How many pounds can Kelly buy with $12?"""
    cost_per_half_pound = 0.6
    total_cost = 12
    pounds = (total_cost / cost_per_half_pound) * 0.5
    result = pounds
    return result

print(solution())