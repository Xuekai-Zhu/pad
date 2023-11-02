def solution():
    """John buys dinner plates and silverware. The silverware cost $20. The dinner plates cost 50% as much as the silverware. How much did he pay for everything?"""
    silverware_cost = 20
    dinner_plate_cost = 0.5 * silverware_cost
    total_cost = silverware_cost + dinner_plate_cost
    result = total_cost
    return result

print(solution())