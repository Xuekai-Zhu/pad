def solution():
    
    dresses_per_hour = 1/12
    total_dresses = 5
    hours_per_week = 4
    dresses_per_week = dresses_per_hour * hours_per_week
    total_weeks = total_dresses / dresses_per_week
    result = total_weeks
    return result

print(solution())