def solution():
    
    sunset_time = 6 * 60  
    daily_increase = 1.2
    days = 40
    total_increase = daily_increase * days
    current_time = 6 * 60 + 10  
    minutes_until_sunset = sunset_time + total_increase - current_time
    result = minutes_until_sunset
    return result

print(solution())