def solution():
    
    mold_cost = 250
    hours_to_make_shoes = 8
    cost_per_hour = 75
    total_cost_of_work = hours_to_make_shoes * cost_per_hour
    cost_of_work_discounted = total_cost_of_work * .8
    total_cost = mold_cost + cost_of_work_discounted
    result = total_cost
    return result

print(solution())