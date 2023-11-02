def solution():
    """Elizabeth wants to buy the steak knives from a bridal registry as a wedding gift. The couple registered for 2 steak knife sets and each set contains 4 steak knives. If Elizabeth buys both sets and they cost $80.00 per set, how much does each single steak knife cost?"""
    sets_of_steak_knives = 2
    steak_knives_per_set = 4
    total_steak_knives = sets_of_steak_knives * steak_knives_per_set
    total_cost = 80 * sets_of_steak_knives
    cost_per_knife = total_cost / total_steak_knives
    result = cost_per_knife
    return result

print(solution())