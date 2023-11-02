def solution():
    """Elysse can carry 3 bags of groceries into her home with each trip from the car. Her brother can carry the same amount. How many trips will it take them to carry 30 bags of groceries?"""
    bags_per_trip = 3
    total_bags = 30
    trips = total_bags / (2 * bags_per_trip)
    # divide by 2 because there are 2 people carrying bags
    result = trips
    return result

print(solution())