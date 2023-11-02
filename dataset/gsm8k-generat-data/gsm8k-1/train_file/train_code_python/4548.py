def solution():
    """Amanda's car takes five fewer minutes to complete the same trip to the beach than the bus. If the bus takes 40 minutes to drive 80 miles to the beach, how many minutes will it take the car to make a round trip?"""
    bus_time = 40
    car_time = bus_time - 5
    round_trip_time = (bus_time + car_time) * 2
    result = round_trip_time
    return result

print(solution())