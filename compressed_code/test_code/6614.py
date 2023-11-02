def solution():
    
    hours_per_day = 2
    days_read = 5
    total_hours_read = hours_per_day * days_read
    pages_per_hour = 50
    pages_read = total_hours_read * pages_per_hour
    pages_read_per_week = pages_read * 7 / 5
    result = pages_read_per_week
    return result

print(solution())