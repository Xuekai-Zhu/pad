def solution():
    
    weeds_per_hour = (10 * 100) / 5  
    seconds_per_hour = 60 * 60
    seconds_per_weed = seconds_per_hour / weeds_per_hour
    result = seconds_per_weed
    return result

print(solution())