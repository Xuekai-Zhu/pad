def solution():
    
    # Define the cost of each bus trip and the number of bus trips per week
    BUS_TRIP_COST = 2.20
    BUS_TRIPS_PER_WEEK = 2 * 5

    # Calculate the total cost of the bus trips for a weekly bus pass
    total_cost = BUS_TRIPS_PER_WEEK * BUS_TRIPS_PER_WEEK * BUS_TRIPS_PER_WEEK * 20

    # Calculate the amount saved by buying a weekly bus pass
    savings = total_cost - 20

    # Display the amount saved
    result = savings
    return result

print(solution())