def solution():
    cost_per_ride_with_pass = 50 / 30  # Cost per ride with a 30-day pass
    cost_per_ride_with_ticket = 2  # Cost per ride with a one-way ticket

    # Calculate the minimum number of rides needed to make the 30-day pass cheaper per ride
    min_rides = int(50 / (2 - cost_per_ride_with_pass)) + 1
    result = min_rides
    return result

print(solution())