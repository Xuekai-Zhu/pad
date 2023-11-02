def solution():
    
    shells_per_day = 10
    total_days = 6
    total_shells = shells_per_day * total_days
    shells_given = 2
    shells_left = total_shells - shells_given
    result = shells_left
    return result

print(solution())