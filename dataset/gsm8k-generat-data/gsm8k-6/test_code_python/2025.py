def solution():
    # Calculate the number of buses leaving the station in a day
    buses_per_day = 12/0.5 # buses leave every half-hour for 12 hours a day
    
    # Calculate the total number of buses leaving the station for 5 days
    total_buses = buses_per_day * 5
    
    result = total_buses
    return result

print(solution())