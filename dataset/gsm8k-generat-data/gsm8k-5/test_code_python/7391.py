def solution():
    # Cost of 2 loads in the washer
    washer_cost = 4 * 2

    # Cost per dryer cycle
    dryer_cost = 0.25 * 4  # $0.25 for 10 minutes, 40 minutes = 4 cycles

    # Total cost of drying all the clothes
    total_dryer_cost = dryer_cost * 3

    # Total cost for wash and dry
    total_cost = washer_cost + total_dryer_cost
    result = total_cost
    return result

print(solution())