def solution():
    """Elizabeth wants to buy the steak knives from a bridal registry as a wedding gift. The couple registered for 2 steak knife sets and each set contains 4 steak knives. If Elizabeth buys both sets and they cost $80.00 per set, how much does each single steak knife cost?"""
    total_sets = 2
    knives_per_set = 4
    set_cost = 80
    total_cost = total_sets * set_cost
    total_knives = total_sets * knives_per_set
    cost_per_knife = total_cost / total_knives
    result = cost_per_knife
    return result

print(solution())