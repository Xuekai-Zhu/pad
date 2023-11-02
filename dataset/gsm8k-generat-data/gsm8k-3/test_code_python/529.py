def solution():
    """A one-way ticket costs $2. A 30-day pass costs $50. What's the minimum number of rides you will need to take every month so that the 30-day pass is strictly cheaper per ride?"""
    # Define the cost of a one-way ticket and a 30-day pass
    ONE_WAY_COST = 2
    THIRTY_DAY_COST = 50

    # Calculate the cost per ride for a one-way ticket
    one_way_cost_per_ride = ONE_WAY_COST

    # Calculate the cost per ride for a 30-day pass
    thirty_day_cost_per_ride = THIRTY_DAY_COST / 30

    # Determine the minimum number of rides required for the 30-day pass to be cheaper per ride
    min_rides = THIRTY_DAY_COST // (ONE_WAY_COST - thirty_day_cost_per_ride) + 1

    # Display the minimum number of rides
    result = min_rides
    return result

print(solution())