def solution():
    """Amanda's car takes five fewer minutes to complete the same trip to the beach than the bus. If the bus takes 40 minutes to drive 80 miles to the beach, how many minutes will it take the car to make a round trip?"""
    # Define the distance to the beach
    distance = 80

    # Define the time it takes for the bus to reach the beach
    bus_time = 40

    # Calculate the speed of the bus
    bus_speed = distance / (bus_time / 60)

    # Calculate the time it takes for the car to reach the beach
    car_time = bus_time - 5

    # Calculate the speed of the car
    car_speed = distance / (car_time / 60)

    # Calculate the time it takes for the car to make a round trip
    round_trip_time = (distance * 2) / car_speed

    # Round the result to the nearest minute
    result = round(round_trip_time)
    return result

print(solution())