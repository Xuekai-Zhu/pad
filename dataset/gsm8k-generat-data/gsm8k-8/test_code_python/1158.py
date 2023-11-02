def solution():
    bags_per_trip = 10
    trips_per_day = 20
    days = 5

    total_trips = trips_per_day * days
    total_bags = bags_per_trip * total_trips

    result = total_bags
    return result

print(solution())