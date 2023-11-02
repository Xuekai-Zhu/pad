def solution():
    """Elysse can carry 3 bags of groceries into her home with each trip from the car. Her brother can carry the same amount. How many trips will it take them to carry 30 bags of groceries?"""
    # Calculate the total number of bags they can carry per trip
    bags_per_trip = 3 + 3  # Elysse + brother

    # Calculate the total number of trips required to carry 30 bags
    trips_required = 30 // bags_per_trip
    if 30 % bags_per_trip != 0:
        trips_required += 1

    # Display the number of trips required
    result = trips_required
    return result

print(solution())