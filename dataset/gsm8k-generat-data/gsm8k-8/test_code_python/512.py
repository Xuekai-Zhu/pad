def solution():
    # Calculate the total number of bags they can carry in one trip
    bags_per_trip = 3 + 3

    # Calculate the total number of trips needed
    total_trips = 30 / bags_per_trip

    # Round up to the nearest whole number of trips
    total_trips = int(total_trips) + (total_trips % 1 > 0)

    result = total_trips
    return result

print(solution())