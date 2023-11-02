def solution():
    """A one-way ticket costs $2. A 30-day pass costs $50. What's the minimum number of rides you will need to take every month so that the 30-day pass is strictly cheaper per ride?"""
    # Define the cost of a one-way ticket and a 30-day pass
    one_way_cost = 2
    thirty_day_cost = 50

    # Calculate the cost per ride for a one-way ticket
    one_way_per_ride = one_way_cost

    # Calculate the cost per ride for a 30-day pass
    thirty_day_per_ride = thirty_day_cost / 30

    # Calculate the minimum number of rides needed to make the 30-day pass cheaper
    min_rides = int(thirty_day_cost / (one_way_per_ride - thirty_day_per_ride)) + 1

    result = min_rides
    return result

print(solution())