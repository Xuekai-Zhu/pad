def solution():
    
    mold_cost = 250
    shoes_time = 8
    shoes_cost = 75 * shoes_time
    total_cost = mold_cost + (0.8 * shoes_cost)
    result = total_cost
    return result

print(solution())