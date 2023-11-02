def solution():
    
    hours_per_day = 6
    days = 7
    num_professionals = 2
    rate_per_hour = 15
    total_hours = hours_per_day * days * num_professionals
    total_cost = total_hours * rate_per_hour
    result = total_cost
    return result

print(solution())