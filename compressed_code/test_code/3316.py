def solution():
    
    days_in_week = 7
    minnie_horses_per_day = days_in_week + 3
    mickey_horses_per_day = (2*minnie_horses_per_day) - 6
    mickey_horses_per_week = mickey_horses_per_day * days_in_week
    result = mickey_horses_per_week
    return result

print(solution())