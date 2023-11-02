def solution():
    
    time_to_bus = 5
    bus_ride = 20
    time_to_work = 5
    total_time_per_trip = time_to_bus + bus_ride + time_to_work
    total_time_per_day = total_time_per_trip * 2
    total_time_per_year = total_time_per_day * 365
    hours_per_year = total_time_per_year / 60
    result = hours_per_year
    return result

print(solution())