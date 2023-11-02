def solution():
    
    current_sleep = 4
    recommended_sleep = 6
    hours_lack_per_day = recommended_sleep - current_sleep
    hours_lack_per_week = hours_lack_per_day * 7
    result = hours_lack_per_week
    return result

print(solution())