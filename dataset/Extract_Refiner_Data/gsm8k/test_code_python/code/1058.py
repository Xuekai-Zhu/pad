def solution():
    
    cast_cost = 200
    visit_time = 0.5 # hours
    visit_cost = cast_cost + (300 * visit_time) + (4 * 30) + (6 * 2) # $6 per hour * 2 hours
    total_cost = visit_cost
    result = total_cost
    return result

print(solution())