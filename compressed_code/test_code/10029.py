def solution():
    
    day1_hours = 2
    day2_hours = day1_hours * 2
    day3_hours = day2_hours - 1
    total_hours = day1_hours + day2_hours + day3_hours
    minutes_per_hour = 60
    total_minutes = total_hours * minutes_per_hour
    result = total_minutes
    return result

print(solution())