def solution():
    """Amanda's car takes five fewer minutes to complete the same trip to the beach than the bus. If the bus takes 40 minutes to drive 80 miles to the beach, how many minutes will it take the car to make a round trip?"""
    bus_time = 40
    bus_distance = 80
    car_time = bus_time - 5
    car_distance = bus_distance * 2
    car_speed = car_distance / (car_time / 60)
    car_time_round = (car_distance / car_speed) * 2
    result = car_time_round
    return result

print(solution())