def solution():
    """John has been having trouble sleeping lately. In the past week he was only able to get 3 hours of sleep on 2 of the days and on the remaining days he was only able to get 60% of the recommended 8 hours of sleep. How much sleep did he get this week?"""
    recommended_sleep = 8
    days_with_3_hours = 2
    days_with_60_percent_sleep = 5
    
    total_sleep = (days_with_3_hours * 3) + (days_with_60_percent_sleep * (recommended_sleep * 0.6))
    result = total_sleep
    return result

print(solution())