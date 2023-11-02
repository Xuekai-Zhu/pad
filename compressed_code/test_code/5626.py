def solution():
    
    hourly_rate = 60
    daily_hours = 3
    num_of_days = 14 
    total_hours = daily_hours * num_of_days
    total_cost = total_hours * hourly_rate
    result = total_cost
    return result

print(solution())