def solution():
    
    initial_snowflakes = 10
    snowflakes_needed = 58
    snowflakes_per_interval = 4
    minutes_per_interval = 5
    
    
    intervals_needed = (snowflakes_needed - initial_snowflakes) / snowflakes_per_interval
    
    
    total_minutes = intervals_needed * minutes_per_interval
    
    result = total_minutes
    return result

print(solution())