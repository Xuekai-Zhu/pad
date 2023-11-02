def solution():
    # Calculate the cost per ride for a one-way ticket
    one_way_cost_per_ride = 2

    # Calculate the cost per ride for a 30-day pass
    thirty_day_cost_per_ride = 50 / 30

    # Calculate the minimum number of rides needed to make the 30-day pass cheaper per ride
    min_rides = int((thirty_day_cost_per_ride * 100) // (one_way_cost_per_ride * 100)) + 1
    result = min_rides
    return result

print(solution())