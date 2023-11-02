def solution():
    
    daily_rate = 50
    weekly_rate = 500
    days_in_week = 14
    if days_in_week < 20:
        
        weeks = 1
        extra_days = 20 - days_in_week
    else:
        
        weeks = 2
        extra_days = 0

    total_cost = weekly_rate * weeks  
    total_cost += extra_days * daily_rate  
    result = total_cost
    return result

print(solution())