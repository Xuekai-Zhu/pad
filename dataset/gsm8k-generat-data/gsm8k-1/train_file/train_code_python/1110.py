def solution():
    """Barbara asked the butcher for 4 1/2 pound steaks that cost $15.00/pound. She also asked for a pound and half of chicken breasts that were $8.00 a pound. How much did she spend at the butchers?"""
    steak_weight = 4.5
    steak_cost_per_pound = 15
    chicken_weight = 1.5
    chicken_cost_per_pound = 8
    total_cost = (steak_weight * steak_cost_per_pound) + (chicken_weight * chicken_cost_per_pound)
    result = total_cost
    return result

print(solution())