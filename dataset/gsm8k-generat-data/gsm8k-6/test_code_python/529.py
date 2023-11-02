def solution():
    # Calculate the cost per ride for a one-way ticket
    one_way_cost_per_ride = 2 
    
    # Calculate the cost per ride for a 30-day pass
    thirty_day_cost_per_ride = 50 / (30*2)  # assuming 2 rides per day

    # Find the minimum number of rides to make the 30-day pass cheaper per ride
    min_rides = int(50/(2 - thirty_day_cost_per_ride)) + 1  # add 1 to round up
    result = min_rides
    return result

print(solution())