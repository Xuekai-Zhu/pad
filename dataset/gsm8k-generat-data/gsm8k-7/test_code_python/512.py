def solution():
    elysse_bags_per_trip = 3
    brother_bags_per_trip = 3
    total_bags = 30

    # Calculate the total number of trips needed for Elysse and her brother combined
    total_trips = total_bags / (elysse_bags_per_trip + brother_bags_per_trip)

    result = total_trips
    return result

print(solution())