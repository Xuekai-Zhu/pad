def solution():
    bags_per_trip = 3  # Elysse and her brother can carry 3 bags each trip
    total_bags = 30  # They need to carry 30 bags in total

    # Calculate the number of trips needed to carry all the bags
    trips_needed = total_bags / (2 * bags_per_trip)  # They are carrying the bags together, so divide by 2

    result = trips_needed
    return result

print(solution())