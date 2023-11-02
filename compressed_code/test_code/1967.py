def solution():
    
    total_points = 0
    total_points += 5 * 2 
    total_points += 10 * 4 
    remaining_points = 100 - total_points 
    throws_allowed = remaining_points // 25 
    result = throws_allowed
    return result

print(solution())