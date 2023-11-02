def solution():
    """Amanda's car takes five fewer minutes to complete the same trip to the beach than the bus. If the bus takes 40 minutes to drive 80 miles to the beach, how many minutes will it take the car to make a round trip?"""
    # Calculate the speed of the bus
    bus_speed = 80 / (40 / 60)  # miles per hour

    # Calculate the time it takes for the car to make the trip to the beach
    car_time_to_beach = (80 / (bus_speed * (5 / 60))) * 60  # in minutes

    # Calculate the time it takes for the car to make the round trip
    car_round_trip_time = car_time_to_beach * 2

    # Display the time it takes for the car to make the round trip
    result = car_round_trip_time
    return result

print(solution())