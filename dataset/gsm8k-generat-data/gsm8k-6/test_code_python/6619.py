def solution():
    # Calculate the number of trips needed to transport all the cattle
    num_trips = 400 // 20  # each truck can carry 20 head of cattle

    # Calculate the distance that the truck will travel in one trip
    distance_per_trip = 60

    # Calculate the total driving time needed for all the trips
    total_driving_time = num_trips * distance_per_trip / 60  # traveling at 60 miles per hour

    result = total_driving_time
    return result

print(solution())