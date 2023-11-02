def solution():
    hours_per_day = 8
    days_per_week = 5
    percent_time = 25
    hours_per_week = hours_per_day * days_per_week
    time_in_math = hours_per_week * (percent_time / 100)
    result = time_in_math
    
    return result

print(solution())