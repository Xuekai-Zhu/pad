def solution():
    
    weekday_time = 30
    saturday_time = weekday_time * 3
    total_time = (weekday_time * 5) + saturday_time
    result = total_time / 60  
    return result

print(solution())