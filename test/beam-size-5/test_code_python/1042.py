def solution():
    
    painters_per_day = 4
    days_per_week = 7
    weeks = 3
    total_painters = painters_per_day * days_per_week * weeks
    hours_per_painter = total_painters / total_painters
    result = hours_per_painter
    return result

print(solution())