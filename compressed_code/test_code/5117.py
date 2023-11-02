def solution():
    
    recommended_sleep = 8
    total_days = 7
    partial_sleep_days = 2
    partial_sleep_hours = 3
    normal_sleep_percentage = 0.6
    normal_sleep_hours = recommended_sleep * normal_sleep_percentage
    normal_sleep_days = total_days - partial_sleep_days
    total_sleep_hours = (partial_sleep_hours * partial_sleep_days) + (normal_sleep_hours * normal_sleep_days)
    result = total_sleep_hours
    return result

print(solution())