def solution():
    
    buses_per_hour = 2
    hours_per_day = 12
    buses_per_day = buses_per_hour * hours_per_day
    days = 5
    total_buses = buses_per_day * days
    result = total_buses
    return result

print(solution())