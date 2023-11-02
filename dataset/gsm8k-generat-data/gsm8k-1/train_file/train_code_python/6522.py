def solution():
    """John buys dinner plates and silverware. The silverware cost $20. The dinner plates cost 50% as much as the silverware. How much did he pay for everything?"""
    silverware_cost = 20
    plate_cost = silverware_cost * 0.5
    total_cost = silverware_cost + plate_cost
    result = total_cost
    return result

print(solution())