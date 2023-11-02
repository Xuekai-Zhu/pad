def solution():
    
    total_ceilings = 28
    painted_this_week = 12
    painted_next_week = painted_this_week * (1/4)
    total_painted = painted_this_week + painted_next_week
    remaining_ceilings = total_ceilings - total_painted
    result = remaining_ceilings
    return result

print(solution())