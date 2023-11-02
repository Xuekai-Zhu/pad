def solution():
    """Elysse can carry 3 bags of groceries into her home with each trip from the car. Her brother can carry the same amount. How many trips will it take them to carry 30 bags of groceries?"""
    # Define the number of bags each person can carry
    bags_per_trip = 3

    # Define the total number of bags
    total_bags = 30

    # Calculate the total number of trips needed
    total_trips = total_bags / (2 * bags_per_trip)

    # Round up to the nearest whole number of trips
    total_trips = math.ceil(total_trips)

    # return the result
    result = total_trips
    return result

print(solution())