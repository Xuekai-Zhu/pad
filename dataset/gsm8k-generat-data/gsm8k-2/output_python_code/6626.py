def solution():
    """John has been having trouble sleeping lately. In the past week he was only able to get 3 hours of sleep on 2 of the days and on the remaining days he was only able to get 60% of the recommended 8 hours of sleep. How much sleep did he get this week?"""
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